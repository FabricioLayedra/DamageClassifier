#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import seaborn as sns


# ### Cosine similarity

# In[15]:


cosine = pd.read_csv("cosine.csv").fillna(0)


# In[16]:


cosine.describe()


# #### LEAST COSINE SIMILARITY

# In[72]:


cosine[(cosine["cosine_similarity"]<0.125)&(cosine["cosine_similarity"]>0)]


# #### MOST COSINE SIMILARITY

# In[74]:


cosine[(cosine["cosine_similarity"]>0.93)]


# In[17]:


sns.distplot(cosine["cosine_similarity"])


# ### Dynamic Time Warping

# In[10]:


dtw = pd.read_csv("dtw_tower.csv")


# In[18]:


dtw.sample()


# In[11]:


dtw.describe()


# In[19]:


sns.distplot(dtw["dtw"])


# ### Events Frecuency 

# In[63]:


hours = pd.read_csv("freq_sub_hours.csv")
days = pd.read_csv("freq_sub_days.csv")


# In[53]:


sns.distplot(days["freq_sub"])


# #### Hours

# In[48]:


import numpy as np
import matplotlib.pyplot as plt
sns.set(style="white")

corr = hours.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(400, 5, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap="RdBu", vmax=1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .7})


# #### Entropy

# In[54]:


entropy = pd.read_csv("entropy.csv")


# In[56]:


entropy.sample(5)


# In[57]:


sns.distplot(entropy["zscore"])


# In[59]:


galo = cosine.merge(dtw,on="GeoId",how="inner")


# In[64]:


mabe = days.merge(hours, on="GeoId", how ="inner")


# In[67]:


oreo = galo.merge(mabe, on="GeoId", how ="inner")


# In[68]:


df = oreo.merge(entropy, left_on = "GeoId",right_on="base",how="inner")


# In[69]:


df.describe()


# In[70]:


import numpy as np
import matplotlib.pyplot as plt
sns.set(style="white")

corr = df.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(400, 5, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap="RdBu", vmax=1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .7})

