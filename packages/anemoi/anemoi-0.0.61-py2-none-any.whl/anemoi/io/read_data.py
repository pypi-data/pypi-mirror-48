import anemoi as an
import pandas as pd
from os import walk


def from_windographer_csv(filename, skiprows=8, na_values=-999, sensors=None):
    if sensors is None:
        header = skiprows
        skiprows = 0
    else:
        header = None

    data = pd.read_csv(filename,
                       index_col=0,
                       infer_datetime_format=True,
                       parse_dates=True,
                       skiprows=skiprows,
                       header=header,
                       na_values=na_values,
                       encoding='iso-8859-1')
    data = data.dropna(axis=1, how='all')

    data.columns = data.columns.str.split(' ', expand=True).get_level_values(0)
    data.columns.name = 'sensor'
    data.index.name = 'stamp'

    if sensors is not None:
        data.columns = sensors
    return data


def from_parquet_files(filename_data, filename_metadata):
    data = pd.read_parquet(filename_data)
    metadata = pd.read_parquet(filename_metadata).T
    name = metadata.columns[0]
    lat = metadata.loc['lat', name]
    lon = metadata.loc['lon', name]
    elev = metadata.loc['elev', name]
    height = metadata.loc['height', name]
    primary_ano = metadata.loc['primary_ano', name]
    primary_vane = metadata.loc['primary_vane', name]
    mast = an.MetMast(data=data,
                      name=name,
                      lat=lat,
                      lon=lon,
                      elev=elev,
                      height=height,
                      primary_ano=primary_ano,
                      primary_vane=primary_vane)
    return mast


def files_in_path(path):
    for (_, _, filenames) in walk(path):
        pass
    return filenames
