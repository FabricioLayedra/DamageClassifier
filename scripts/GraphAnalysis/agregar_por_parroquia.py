#!/usr/bin/env python
# coding: utf-8

"""Script para, dado el archivo de indegrees, agregarlo por parroquias
Command-line: python3 agregar_por_parroquia.py in_degrees_file output_file operation
operation puede ser sum, geomean (promedio geometrico)
"""

import pandas as pd
import sys
from scipy import stats
import numpy as np

def geo_mean(iterable):
    a = [number for number in iterable if number>0]
    a = np.asarray(a)
    if(len(a)==0):
    	return 0.0
    return stats.gmean(a)

file = sys.argv[1] #in_degrees_file
output_file = sys.argv[2] #output file
operation = sys.argv[3] #operation
df_eventos = pd.read_csv("../../data/eventos.csv", encoding = "ISO-8859-1")


#Obtener del dataset entero, un dataframe con las parroquias y geo ids de evento y de cliente
df_parroquias = df_eventos[["GeoIdEvento","ParroquiaEvento","ParroquiaCliente","GeoIdCliente","ProvinciaCliente","ProvinciaEvento"]]
parroquias_evento = df_parroquias[["GeoIdEvento","ParroquiaEvento", "ProvinciaEvento"]].drop_duplicates().reset_index()
parroquias_cliente = df_parroquias[["ParroquiaCliente","GeoIdCliente", "ProvinciaCliente"]].drop_duplicates().reset_index()

#dejar solo las que son de manabi
parroquias_evento = parroquias_evento.loc[parroquias_evento["ProvinciaEvento"]=="MANABI"]
parroquias_evento = parroquias_evento.drop("ProvinciaEvento", axis=1)
parroquias_evento = parroquias_evento.drop("index", axis=1)
parroquias_cliente = parroquias_cliente.loc[parroquias_cliente["ProvinciaCliente"]=="MANABI"]
parroquias_cliente = parroquias_cliente.drop("ProvinciaCliente", axis=1)
parroquias_cliente = parroquias_cliente.drop("index", axis=1)

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

#---- aqui se tiene que comentar la linea que no sea igual al encabeza del csv de los scores
#indegrees_with_parr = indegrees_with_parr[["Parroquia","InDegree"]]
indegrees_with_parr = indegrees_with_parr[["Parroquia","TowerRank"]]

if (operation == "sum"):
#cuando ses agrupa por parroquia, se suma el indegree
	indegrees_by_parr = indegrees_with_parr.groupby("Parroquia").sum().reset_index()
else:
	indegrees_by_parr = indegrees_with_parr.groupby("Parroquia").aggregate(geo_mean).reset_index()
indegrees_by_parr.to_csv(output_file, index=False)
print(output_file)
