
# coding: utf-8

# In[9]:


import pandas as pd
from math import radians, sin, cos, acos


# In[10]:


def distance_from_coords(row):
    slat = radians(row["LatitudCliente"])
    slon = radians(row["LongitudCliente"])
    elat = radians(row["LatitudEvento"])
    elon = radians(row["LongitudEvento"])
    dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    return dist


# In[11]:


df_eventos = pd.read_csv("../../eventos.csv", encoding = "ISO-8859-1", parse_dates=['FechaEvento'], infer_datetime_format=True)
df_eventos_abril = df_eventos[(df_eventos["FechaEvento"] == pd.datetime(2016,4,15)) ]
df_eventos_abril


# In[12]:



df_eventos_abril["Distancia"] = df_eventos_abril.apply(lambda row: distance_from_coords(row),axis=1)
df_eventos_abril["Distancia"]

