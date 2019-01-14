#!/usr/bin/env python
# coding: utf-8

# In[85]:


#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
def read_dataset(file):
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
        'ProvinciaEvento': 'category'}

    df_eventos = pd.read_csv(file, encoding = "ISO-8859-1", dtype=col_dtypes, parse_dates=['FechaEvento'], infer_datetime_format=True)
    return df_eventos


# In[107]:


def distanciaGeografica(dataframe):

    try:
        lat1 = float(dataframe["LatitudCliente"])
        lat2 = float(dataframe["LatitudEvento"])
        long1 = float(dataframe["LongitudCliente"])
        long2 = float(dataframe["LongitudEvento"])
        r = 6371
        c = math.pi/180

        d= 2*r*math.asin(math.sqrt(math.sin(c*(lat2-lat1)/2)**2 + math.cos(c*lat1) * math.cos(c*lat2) * math.sin(c*(long2-long1)/2)**2))
        return round(d,2)
    except:
        pass


def getEntropy(dataset,event_col,home_col,output,file):
    eventos=set(dataset[event_col])
    homes=set(dataset[home_col])
    
    frecuencias = dict()

    eventos = list(eventos)

    for evento in  eventos:
        frecuencias[evento]= np.zeros(len(homes)) 
    
    #print (frecuencias.keys())
    homes = list(homes)
    #print(homes)

    f = open (file)
    f.readline()
    for line in f:
        line = line.strip()
        values = line.split(",")
        try:
            frecuencias[int(values[-1])][homes.index(int(values[-2]))]+= 1
        except: 
            pass
    f.close()

    entropias = {}

    for base in frecuencias: 
        probs = frecuencias[base]/frecuencias[base].sum()
        #preguntar
        probs = probs[probs>0]
        shannon = probs * - np.log(probs)
        entropia = shannon.sum()/len(probs)
        #if(entropia!=0.0):
            #print(base)
            #entropias[base] = entropia
        entropias[base] = entropia

    f2 = open(output, 'w')
    f2.write('base,enthropy\n')
    for entropy in entropias:
        f2.write(str(entropy)+","+str(entropias[entropy])+"\n")
    f2.close()


# In[3]:


df = pd.read_csv("../DataComprimida/EventosManabi.csv")


# In[ ]:


del df["BaseEvento"]
del df["BaseCliente"]
del dataset["ID"]


# In[47]:


dataset = df.groupby(["FechaEvento","Hora","ProvinciaCliente","CantonCliente","CiudadCliente","ParroquiaCliente","LatitudCliente","LongitudCliente","NombreSitioEvento","ProvinciaEvento","CantonEvento","CiudadEvento","ParroquiaEvento","LatitudEvento","LongitudEvento"]).sum().reset_index()


# In[6]:


dataset.to_csv("events_filtered.csv",index=False)


# In[48]:


cliente = dataset[["LatitudCliente","LongitudCliente"]].rename(columns={"LatitudCliente":"lat","LongitudCliente":"lon"})
evento = dataset[["LatitudEvento","LongitudEvento"]].rename(columns={"LatitudEvento":"lat","LongitudEvento":"lon"})


# In[49]:


points = pd.concat([cliente,evento])


# In[50]:


points2 = points.drop_duplicates().reset_index()


# In[54]:


del(points2["index"])
points2["GEO_ID"] = points2.index + 1


# In[55]:


points2.head()


# In[56]:


new_df = pd.merge(dataset, points2,  how='left', left_on=["LatitudCliente","LongitudCliente"], right_on = ['lat','lon'])


# In[57]:


new_df = pd.merge(new_df, points2,  how='left', left_on=["LatitudEvento","LongitudEvento"], right_on = ['lat','lon'])


# In[59]:


del new_df["lat_x"]
del new_df["lon_x"]
del new_df["lat_y"]
del new_df["lon_y"]


# In[61]:


new_df = new_df.rename(columns={"GEO_ID_x":"GeoIdCliente","GEO_ID_y":"GeoIdEvento"})


# In[63]:


new_df.to_csv("eventos.csv",index=False)


# In[72]:


new_df.head()


# In[76]:


april15 = new_df[new_df["FechaEvento"]=="2016-04-15"]
april16 = new_df[new_df["FechaEvento"]=="2016-04-16"]
april17 = new_df[new_df["FechaEvento"]=="2016-04-17"]


# In[108]:


getEntropy(april15,"GeoIdEvento","GeoIdCliente","entropy_15.csv","eventos.csv")
entropy15 = pd.read_csv("entropy_15.csv")


# In[114]:


len(entropy15)


# In[113]:


getEntropy(april16,"GeoIdEvento","GeoIdCliente","entropy_16.csv","eventos.csv")
entropy16 = pd.read_csv("entropy_16.csv")


# In[115]:


len(entropy16)


# In[117]:


getEntropy(april17,"GeoIdEvento","GeoIdCliente","entropy_17.csv","eventos.csv")
entropy17 = pd.read_csv("entropy_17.csv")


# In[118]:


len(entropy17)


# In[122]:


entropy = entropy15.merge(entropy17,on="base",how="outer").fillna(0)


# In[125]:


entropy["diff"]=entropy["enthropy_y"] - entropy["enthropy_x"]


# In[129]:


import seaborn as sns
from scipy import stats


# In[131]:


sns.distplot(stats.zscore(entropy["diff"]))
plt.show()


# In[133]:


entropy = entropy.rename(columns={"enthropy_x":"entropy15april","enthropy_y":"entropy17april"}) 


# In[135]:


entropy["zscore"] = stats.zscore(entropy["diff"])


# In[137]:


entropy.to_csv("entropy.csv",index=False)

