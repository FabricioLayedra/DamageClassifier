#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import seaborn as sns
import networkx as nx
import matplotlib.pyplot as plt


# In[34]:


#read the graph with indegrees of april 15
df_15 = pd.read_csv("output/in_degrees_graph_20160415.csv")
sns.distplot(df_15["InDegree"], vertical=True)


# In[35]:


#read the graph with indegrees of april 17
df_17 = pd.read_csv("output/in_degrees_graph_20160417.csv")
sns.distplot(df_17["InDegree"], vertical=True)


# In[43]:


#read the entire csv of events
df_eventos = pd.read_csv("../../eventos.csv", encoding = "ISO-8859-1", parse_dates=['FechaEvento'], infer_datetime_format=True)


# In[36]:


df_15 = df_15.rename(columns={"GeoId":"GeoIdEvento"})
#get just the item from april 15
df_eventos_abril_15 = df_eventos[(df_eventos["FechaEvento"] == pd.datetime(2016,4,15)) ]
#unify the data of the indegrees with the whole dataset
df = pd.merge(df_eventos_abril_15,df_15, how="inner", on="GeoIdEvento")
#takw just the columns we care, this are, indegree and id
df = df[["GeoIdEvento","InDegree"]]
#remember to drop duplicates, as there are a lot since for one tower there are various events
torres_eventos_15 = df.drop_duplicates()
sns.distplot(torres_eventos_15["InDegree"], vertical=True)


# In[48]:



df_17 = df_17.rename(columns={"GeoId":"GeoIdEvento"})
#escojo los eventos que se dieron el 17
df_eventos_abril_17 = df_eventos[(df_eventos["FechaEvento"] == pd.datetime(2016,4,17)) ]

df = pd.merge(df_eventos_abril_17,df_17, how="inner", on="GeoIdEvento")
df = df[["GeoIdEvento","InDegree"]]
torres_eventos_17 = df.drop_duplicates()
print(torres_eventos_17["GeoIdEvento"].nunique())
sns.distplot(torres_eventos_17["InDegree"], vertical=True)


# In[38]:


df.shape


# In[39]:


#analizar in degree de grafo del 15
#degree_sequence = torres_eventos_15["InDegree"].tolist()
#degree_sequence = sorted(degree_sequence)


# In[40]:


fig, ax = plt.subplots()
torres_eventos_15.hist(column='InDegree', ax=ax)
#ax.set_yscale('log')
#ax.set_xscale('log')


# In[41]:


#analizar in degree del grafo del 17 , recordar que este tiene mas nodos
ax = torres_eventos_17.hist(column='InDegree', grid=False, figsize=(7,5), color='#86bf91', zorder=2, rwidth=0.9)
ax = ax[0]
for x in ax:

    # Despine
    x.spines['right'].set_visible(False)
    x.spines['top'].set_visible(False)
    x.spines['left'].set_visible(False)

    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)
    # Set x-axis label
    x.set_xlabel("In degree", labelpad=20, weight='bold', size=12)

    # Set y-axis label
    x.set_ylabel("Number of nodes", labelpad=20, weight='bold', size=12)


# In[58]:


#unificar en una columna la diferencia entre los indegrees, hay 139 torres para el 15 y 109 para el 17
torres_eventos_17 = torres_eventos_17.rename(columns={"InDegree":"InDegree_17"})
torres_eventos_15 = torres_eventos_15.rename(columns={"InDegree":"InDegree_15"})
data_15_17 = pd.merge(torres_eventos_15,torres_eventos_17,how="outer",on="GeoIdEvento")
data_15_17 = data_15_17.fillna(0)
data_15_17["InDegreeDifference"] = data_15_17["InDegree_17"]-data_15_17["InDegree_15"]
data_15_17.to_csv("./output/degree_difference.csv", encoding='utf-8', index=False)
data_15_17

