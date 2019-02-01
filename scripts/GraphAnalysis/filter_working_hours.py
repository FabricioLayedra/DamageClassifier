#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd


# In[22]:


df_eventos = pd.read_csv("output/distancias_20160415.csv")


# In[23]:


df_eventos.tail(5)


# In[24]:


df_working_hours = df_eventos[(df_eventos["Hora"]>6) & (df_eventos["Hora"]<23)]
df_working_hours = df_working_hours.drop("Index", axis=1)


# In[25]:


df_working_hours.shape


# In[26]:


df_working_hours.head(1)


# In[27]:


df_working_hours.to_csv("output/working_hours_20160415.csv", index=True)

