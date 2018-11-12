
# coding: utf-8

# In[78]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm


# In[79]:


def beautify(row):
    row["Afectacion"]


# In[87]:


#merge all data
entropy = pd.read_csv("../utils/entropy.csv", encoding = "ISO-8859-1")
entropy = entropy.rename(columns={"base":"GeoIdEvento"})
entropy = entropy[["GeoIdEvento","diff","zscore"]]
dtw = pd.read_csv("../utils/dtw_tower.csv", encoding = "ISO-8859-1")
dtw = dtw.rename(columns={"GeoId":"GeoIdEvento"})
freq_sub_hours = pd.read_csv("../utils/freq_sub_hours.csv", encoding = "ISO-8859-1")
freq_sub_hours = freq_sub_hours.rename(columns={"GeoId":"GeoIdEvento"})
degree_difference = pd.read_csv("../utils/degree_difference.csv", encoding = "ISO-8859-1")
degree_difference = degree_difference[["GeoIdEvento","InDegreeDifference"]]
etiquetas = pd.read_csv("/home/belen/github/DamageClassifier/utils/manabi-parroquias-shapes/manabi-parroquias-afectacion.csv", encoding = "ISO-8859-1")
etiquetas = etiquetas.rename(columns={"CANTÃ³N":"CANTON", "NOMBRE":"ParroquiaEvento"})
#etiquetas["ParroquiaEvento"]
#etiquetas["ParroquiaEvento"] = etiquetas["ParroquiaEvento"].apply(lambda x: x.title())
etiquetas = etiquetas.replace(np.nan, 'Desconocido', regex=True)
etiquetas["AFECTACION"] = etiquetas["AFECTACION"].apply(lambda x: x.title())
etiquetas = etiquetas[["ParroquiaEvento","AFECTACION"]]
etiquetas["AFECTACION"].value_counts()


# In[81]:


data_entropy_dtw = pd.merge(entropy,dtw,how="inner",on="GeoIdEvento")
data_with_freqs_hour = pd.merge(data_entropy_dtw, freq_sub_hours, how = "inner", on="GeoIdEvento")
data_with_degree = pd.merge(data_with_freqs_hour, degree_difference, how = "inner", on="GeoIdEvento")

df_eventos = pd.read_csv("../eventos.csv", encoding = "ISO-8859-1")
df_eventos = df_eventos[["GeoIdEvento","ParroquiaEvento"]]
df_eventos = df_eventos.drop_duplicates()
data_with_villages = pd.merge(data_with_degree, df_eventos, how = "inner", on="GeoIdEvento")
data_with_tags = pd.merge(data_with_villages, etiquetas, how = "left", on="ParroquiaEvento")
data_with_tags


# In[82]:


X
Y
# Fit and make the predictions by the model
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary()

