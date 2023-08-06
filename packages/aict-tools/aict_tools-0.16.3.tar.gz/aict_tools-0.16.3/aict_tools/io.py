import os
from sklearn.externals import joblib
import logging
import numpy as np
from fact.io import read_data, h5py_get_n_rows
import pandas as pd
import h5py
import click

from .feature_generation import feature_generation
from . import __version__


__all__ = [
    'drop_prediction_column',
    'read_telescope_data',
    'read_telescope_data_chunked',
    'save_model',
]


log = logging.getLogger(__name__)


def drop_prediction_column(data_path, group_name, column_name, yes=True):
    '''
    Deletes prediction columns in a h5py file if the columns exist.
    Including 'mean' and 'std' columns.
    '''
    with h5py.File(data_path, 'r+') as f:

        if group_name not in f.keys():
            return

        columns = f[group_name].keys()
        if column_name in columns:
            if not yes:
                click.confirm(
                    f'Column \"{column_name}\" exists in file, overwrite?', abort=True,
                )

            del f[group_name][column_name]

        if column_name + '_std' in columns:
            del f[group_name][column_name + '_std']
        if column_name + '_mean' in columns:
            del f[group_name][column_name + '_mean']


def read_telescope_data_chunked(path, aict_config, chunksize, columns, feature_generation_config=None):
    '''
    Reads data from hdf5 file given as PATH and yields dataframes for each chunk
    '''
    return TelescopeDataIterator(
        path,
        aict_config,
        chunksize,
        columns,
        feature_generation_config=feature_generation_config,
    )


class TelescopeDataIterator:

    def __init__(
        self,
        path,
        aict_config,
        chunksize,
        columns,
        feature_generation_config=None,
    ):
        self.aict_config = aict_config
        self.columns = columns
        self.feature_generation_config = feature_generation_config
        self.n_rows = h5py_get_n_rows(path, aict_config.telescope_events_key)
        self.path = path
        if chunksize:
            self.chunksize = chunksize
            self.n_chunks = int(np.ceil(self.n_rows / chunksize))
        else:
            self.n_chunks = 1
            self.chunksize = self.n_rows
        log.info('Splitting data into {} chunks'.format(self.n_chunks))

        self.current_chunk = 0

    def __len__(self):
        return self.n_chunks

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_chunk == self.n_chunks:
            raise StopIteration

        chunk = self.current_chunk
        start = chunk * self.chunksize
        end = min(self.n_rows, (chunk + 1) * self.chunksize)
        self.current_chunk += 1

        df = read_telescope_data(
            self.path,
            aict_config=self.aict_config,
            columns=self.columns,
            first=start,
            last=end
        )
        df.index = np.arange(start, end)

        if self.feature_generation_config:
            feature_generation(df, self.feature_generation_config, inplace=True)

        return df, start, end


def read_telescope_data(path, aict_config, columns, feature_generation_config=None, n_sample=None, first=None, last=None):
    '''
    Read given columns from data and perform a random sample if n_sample is supplied.
    Returns a single pandas data frame
    '''
    telescope_event_columns = None
    array_event_columns = None
    if aict_config.has_multiple_telescopes:
        join_keys = [aict_config.run_id_column, aict_config.array_event_id_column]
        if columns:
            with h5py.File(path, 'r') as f:
                array_event_columns = set(f[aict_config.array_events_key].keys()) & set(columns)
                telescope_event_columns = set(f[aict_config.telescope_events_key].keys()) & set(columns)
                array_event_columns |= set(join_keys)
                telescope_event_columns |= set(join_keys)

        telescope_events = read_data(
            file_path=path,
            key=aict_config.telescope_events_key,
            columns=telescope_event_columns,
            first=first,
            last=last,
        )
        array_events = read_data(
            file_path=path,
            key=aict_config.array_events_key,
            columns=array_event_columns,
        )

        df = pd.merge(left=array_events, right=telescope_events, left_on=join_keys, right_on=join_keys)

    else:
        df = read_data(
            file_path=path,
            key=aict_config.telescope_events_key,
            columns=columns,
            first=first,
            last=last,
        )

    if n_sample is not None:
        if n_sample > len(df):
            raise ValueError(
                'number of sampled events'
                ' {} must be smaller than number events in file {} ({})'
                .format(n_sample, path, len(df))
            )
        log.info('Randomly sample {} events'.format(n_sample))
        state = np.random.RandomState()
        state.set_state(np.random.get_state())
        df = df.sample(n_sample, random_state=state)

    # generate features if given in config
    if feature_generation_config:
        feature_generation(df, feature_generation_config, inplace=True)

    return df


def save_model(model, feature_names, model_path, label_text='label'):
    p, extension = os.path.splitext(model_path)
    model.feature_names = feature_names
    pickle_path = p + '.pkl'

    if extension == '.pmml':
        try:
            from sklearn2pmml import sklearn2pmml, PMMLPipeline
        except ImportError:
            raise ImportError(
                'You need to install `sklearn2pmml` to store models in pmml format'
            )

        pipeline = PMMLPipeline([
            ('model', model)
        ])
        pipeline.target_field = label_text
        pipeline.active_fields = np.array(feature_names)
        sklearn2pmml(pipeline, model_path)

    elif extension == '.onnx':

        try:
            from skl2onnx import convert_sklearn
            from skl2onnx.common.data_types import FloatTensorType
            from skl2onnx.helpers.onnx_helper import select_model_inputs_outputs
            from onnx.onnx_pb import StringStringEntryProto
        except ImportError:
            raise ImportError(
                'You need to install `skl2onnx` to store models in onnx format'
            )

        onnx = convert_sklearn(
            model,
            name=label_text,
            initial_types=[('input', FloatTensorType((1, len(feature_names))))],
            doc_string='Model created by aict-tools to estimate {}'.format(label_text),
        )
        metadata = dict(
            model_author='aict-tools',
            aict_tools_version=__version__,
            feature_names=','.join(feature_names),
        )
        for key, value in metadata.items():
            onnx.metadata_props.append(StringStringEntryProto(key=key, value=value))

        # this makes sure we only get the scores and that they are numpy arrays and not
        # a list of dicts
        if hasattr(model, 'predict_proba'):
            onnx = select_model_inputs_outputs(onnx, ['probabilities'])

        with open(model_path, 'wb') as f:
            f.write(onnx.SerializeToString())
    else:
        pickle_path = model_path

    # Always store the pickle dump,just in case
    joblib.dump(model, pickle_path, compress=4)


def append_to_h5py(f, array, group, key):
    '''
    Write numpy array to h5py hdf5 file
    '''
    group = f.require_group(group)  # create if not exists

    max_shape = list(array.shape)
    max_shape[0] = None

    if key not in group.keys():
        group.create_dataset(
            key,
            data=array,
            maxshape=tuple(max_shape),
        )
    else:
        n_existing = group[key].shape[0]
        n_new = array.shape[0]

        group[key].resize(n_existing + n_new, axis=0)
        group[key][n_existing:n_existing + n_new] = array


def copy_runs_group(infile, outfile):
    for key in ('runs', 'corsika_runs'):
        if key in infile:
            log.info('Copying group "{}"'.format(key))
            infile.copy(key, outfile)
