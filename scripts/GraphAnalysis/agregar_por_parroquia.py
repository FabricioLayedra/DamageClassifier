#!/usr/bin/env python
# coding: utf-8

"""Script para, dado el archivo de indegrees, agregarlo por parroquias"""

import pandas as pd
import sys


file = sys.argv[1]
output_file = sys.argv[2]
df_eventos = pd.read_csv("../../data/eventos.csv", encoding = "ISO-8859-1")


#Obtener del dataset entero, un dataframe con las parroquias y geo ids de evento y de cliente
df_parroquias = df_eventos[["GeoIdEvento","ParroquiaEvento","ParroquiaCliente","GeoIdCliente"]]
parroquias_evento = df_parroquias[["GeoIdEvento","ParroquiaEvento"]].drop_duplicates().reset_index()
parroquias_cliente = df_parroquias[["ParroquiaCliente","GeoIdCliente"]].drop_duplicates().reset_index()
#Hay que renombrar las columnas para luego poder concatenar
parroquias_evento = parroquias_evento.rename(columns={"GeoIdEvento":"GeoId","ParroquiaEvento": "Parroquia"})
parroquias_cliente = parroquias_cliente.rename(columns={"GeoIdCliente":"GeoId","ParroquiaCliente": "Parroquia"})

parroquias = pd.concat([parroquias_evento,parroquias_cliente])
#Finalmente podemos unificar y lograr un dataframe con todas las parroquias y los geoids
parroquias = parroquias.drop_duplicates()
#print(parroquias.shape)
parroquias = parroquias[["GeoId","Parroquia"]]

#Obtener un dataframe a partir del archivo con id_torre,indegree
df_indegrees = pd.read_csv(file)

#Hacer match entre los geoids, para poder asignar las parroquias a las torres
indegrees_with_parr = pd.merge(parroquias,df_indegrees, how = "left", on="GeoId")
indegrees_with_parr = indegrees_with_parr.dropna().drop_duplicates()
indegrees_with_parr = indegrees_with_parr[["Parroquia","InDegree"]]
indegrees_by_parr = indegrees_with_parr.groupby("Parroquia").sum().reset_index()
indegrees_by_parr.to_csv(output_file, index=False)

