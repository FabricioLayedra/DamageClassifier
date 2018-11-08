
# coding: utf-8

# In[10]:


import pandas as pd
import geopy.distance
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:


def distance_from_coords(row):
    
    slat = row["LatitudCliente"]
    slon = row["LongitudCliente"]
    elat = row["LatitudEvento"]
    elon = row["LongitudEvento"]
    coords1 = (slat,slon)
    coords2 = (elat,elon)
    
    #dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    return geopy.distance.geodesic(coords1,coords2).km


# In[12]:


df_eventos = pd.read_csv("../../eventos.csv", encoding = "ISO-8859-1", parse_dates=['FechaEvento'], infer_datetime_format=True)
#here replace date as you wish
df_eventos_abril = df_eventos[(df_eventos["FechaEvento"] == pd.datetime(2016,4,15)) ]
df_eventos.shape


# In[13]:



df_eventos_abril["Distancia"] = df_eventos_abril.apply(lambda row: distance_from_coords(row),axis=1)
df_eventos_abril["Distancia"]


# In[14]:


sns.distplot(df_eventos_abril['Distancia'], hist=True, kde=True, 
             bins=int(18), color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})


# In[18]:


df_eventos_abril.shape
df_eventos_abril.describe()
#df_eventos_abril.loc[df_eventos_abril["Distancia"]>2000,"Distancia"] = 12345678910
#here replace file name as you wish
#df_eventos_abril.to_csv("eventos_con_distancia_20160417.csv", sep=',')


# In[16]:


clientes = df_eventos_abril["GeoIdCliente"].rename(columns={"GeoIdCliente":"TorreId"})
eventos = df_eventos_abril["GeoIdEvento"].rename(columns={"GeoIdEvento":"TorreId"})
torres = pd.concat([clientes,eventos])
torres = torres.drop_duplicates().reset_index()
torres.shape


# In[19]:


df_16 = df_eventos[(df_eventos["FechaEvento"] == pd.datetime(2016,4,16)) ]
df_16 = df_16.groupby(by="Hora").sum

