
# coding: utf-8

# In[8]:


import pandas as pd
import geopy.distance
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


def distance_from_coords(row):
    
    slat = row["LatitudCliente"]
    slon = row["LongitudCliente"]
    elat = row["LatitudEvento"]
    elon = row["LongitudEvento"]
    coords1 = (slat,slon)
    coords2 = (elat,elon)
    
    #dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    return geopy.distance.geodesic(coords1,coords2).km


# In[10]:


df_eventos = pd.read_csv("../../eventos.csv", encoding = "ISO-8859-1", parse_dates=['FechaEvento'], infer_datetime_format=True)
df_eventos_abril = df_eventos[(df_eventos["FechaEvento"] == pd.datetime(2016,4,15)) ]


# In[11]:



df_eventos_abril["Distancia"] = df_eventos_abril.apply(lambda row: distance_from_coords(row),axis=1)
df_eventos_abril["Distancia"]


# In[12]:


sns.distplot(df_eventos_abril['Distancia'], hist=True, kde=True, 
             bins=int(18), color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})


# In[13]:


#df_eventos_abril.loc[df_eventos_abril["Distancia"]>2000,"Distancia"] = 12345678910
#df_eventos_abril.to_csv("eventos_con_distancia.csv", sep=',')


# In[14]:


df_eventos_abril.loc[df_eventos_abril["FechaEvento"]=="2016-04-17"]

