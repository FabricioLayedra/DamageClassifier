#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd


# In[17]:


df_eventos = pd.read_csv("../data/eventos.csv", encoding = "ISO-8859-1")


# In[18]:


df_parroquias = df_eventos[["GeoIdEvento","ParroquiaEvento","ParroquiaCliente","GeoIdCliente","ProvinciaCliente","ProvinciaEvento"]]
parroquias_evento = df_parroquias[["GeoIdEvento","ParroquiaEvento", "ProvinciaEvento"]].drop_duplicates().reset_index()
parroquias_cliente = df_parroquias[["ParroquiaCliente","GeoIdCliente", "ProvinciaCliente"]].drop_duplicates().reset_index()


# In[19]:


#dejar solo las que son de manabi
parroquias_evento = parroquias_evento.loc[parroquias_evento["ProvinciaEvento"]=="MANABI"]
parroquias_evento = parroquias_evento.drop("ProvinciaEvento", axis=1)
parroquias_evento = parroquias_evento.drop("index", axis=1)
parroquias_cliente = parroquias_cliente.loc[parroquias_cliente["ProvinciaCliente"]=="MANABI"]
parroquias_cliente = parroquias_cliente.drop("ProvinciaCliente", axis=1)
parroquias_cliente = parroquias_cliente.drop("index", axis=1)


# In[20]:


#Hay que renombrar las columnas para luego poder concatenar
parroquias_evento = parroquias_evento.rename(columns={"GeoIdEvento":"GeoId","ParroquiaEvento": "Parroquia"})
parroquias_cliente = parroquias_cliente.rename(columns={"GeoIdCliente":"GeoId","ParroquiaCliente": "Parroquia"})

parroquias = pd.concat([parroquias_evento,parroquias_cliente])
#Finalmente podemos unificar y lograr un dataframe con todas las parroquias y los geoids
parroquias = parroquias["Parroquia"].drop_duplicates()
parroquias.to_csv("parroquias_manabi.txt",index=False)


# In[ ]:





# In[ ]:




