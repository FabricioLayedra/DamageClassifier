#!/usr/bin/env python
# coding: utf-8


import pandas as pd

def read_dataset():
    col_dtypes = {'BaseCliente': 'uint16','BaseEvento': 'uint16','CantidadClientes': 'uint8','CantonCliente': 'category','CantonEvento': 'category',
        'CiudadCliente': 'category',
        'CiudadEvento': 'category',
        'Hora': 'uint8',
        'ID': 'uint32',
        'LatitudCliente': 'float64',
        'LatitudEvento': 'float64',
        'LongitudCliente': 'float64',
        'LongitudEvento': 'float64',
        'NombreSitioEvento': 'category',
        'ParroquiaCliente': 'category',
        'ParroquiaEvento': 'category',
        'ProvinciaCliente': 'category',
        'ProvinciaEvento': 'category',
        'GeoIdCliente':'uint32',
        'GeoIdEvento':'uint32'}

    df_eventos = pd.read_csv("../eventos.csv", encoding = "ISO-8859-1", dtype=col_dtypes, parse_dates=['FechaEvento'], infer_datetime_format=True)
    return df_eventos

df = read_dataset()

df["BaseCliente"] = df["BaseCliente"].apply(lambda x: int(str(x)[-3:]))

df["BaseEvento"] = df["BaseEvento"].apply(lambda x: int(str(x)[-3:]))

df = df.iloc[:,1:]

df.to_csv("eventos_dataset.csv",index=False)