#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
from scipy import stats
import numpy as np


# In[55]:


def geo_mean(iterable):
    a = []
    for number in iterable:
        a.append(number+1 if number==0 else number)
    #print(a)
    a = np.asarray(a)
    return stats.gmean(a)-1


# In[56]:


df = pd.read_csv("../data/rdgManabi_3.csv")
df = df[["Parroquia","rs15a","rs16a","rs17a"]]
df


# In[57]:


risc_by_parr = df.groupby("Parroquia").aggregate(geo_mean)
risc_by_parr


# In[59]:


risc_by_parr.reset_index().to_csv("../data/risc_agrupado.csv",index=False)

