
# coding: utf-8

# In[31]:


import pandas as pd
import seaborn as sns


# In[32]:


df_15 = pd.read_csv("output/in_degrees_graph_1.csv")
sns.distplot(df_15["InDegree"], vertical=True)


# In[33]:


df_17 = pd.read_csv("output/in_degrees_graph_2.csv")
sns.distplot(df_17["InDegree"], vertical=True)


# In[47]:


df_eventos = pd.read_csv("../../eventos.csv", encoding = "ISO-8859-1", parse_dates=['FechaEvento'], infer_datetime_format=True)

df_15 = df_15.rename(columns={"GeoId":"GeoIdEvento"})
df_eventos_abril_15 = df_eventos[(df_eventos["FechaEvento"] == pd.datetime(2016,4,15)) ]
df = pd.merge(df_eventos_abril_15,df_15, how="inner", on="GeoIdEvento")
df = df[["GeoIdEvento","InDegree"]]
df = df.drop_duplicates()
sns.distplot(df["InDegree"], vertical=True)


# In[48]:



df_17 = df_17.rename(columns={"GeoId":"GeoIdEvento"})
df_eventos_abril_17 = df_eventos[(df_eventos["FechaEvento"] == pd.datetime(2016,4,17)) ]
df = pd.merge(df_eventos_abril_17,df_17, how="inner", on="GeoIdEvento")
df = df[["GeoIdEvento","InDegree"]]
df = df.drop_duplicates()
sns.distplot(df["InDegree"], vertical=True)


# In[49]:


df.shape

