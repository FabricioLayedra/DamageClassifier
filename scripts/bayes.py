#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm


# In[ ]:


'''
Resources
https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60
'''


# In[87]:


""""#merge all data
entropy = pd.read_csv("../data/entropy.csv", encoding = "ISO-8859-1")
entropy = entropy.rename(columns={"base":"GeoIdEvento"})
entropy = entropy[["GeoIdEvento","diff","zscore"]]
dtw = pd.read_csv("../data/dtw_tower.csv", encoding = "ISO-8859-1")
dtw = dtw.rename(columns={"GeoId":"GeoIdEvento"})
freq_sub_hours = pd.read_csv("../data/freq_sub_hours.csv", encoding = "ISO-8859-1")
freq_sub_hours = freq_sub_hours.rename(columns={"GeoId":"GeoIdEvento"})
degree_difference = pd.read_csv("../data/degree_difference.csv", encoding = "ISO-8859-1")
degree_difference = degree_difference[["GeoIdEvento","InDegreeDifference"]]
etiquetas = pd.read_csv("/home/belen/github/DamageClassifier/utils/manabi-parroquias-shapes/manabi-parroquias-afectacion.csv", encoding = "ISO-8859-1")
etiquetas = etiquetas.rename(columns={"CANTÃ³N":"CANTON", "NOMBRE":"ParroquiaEvento"})
#etiquetas["ParroquiaEvento"]
#etiquetas["ParroquiaEvento"] = etiquetas["ParroquiaEvento"].apply(lambda x: x.title())

etiquetas = etiquetas.replace(np.nan, 'Desconocido', regex=True)
etiquetas["AFECTACION"] = etiquetas["AFECTACION"].apply(lambda x: x.title())
etiquetas = etiquetas[["ParroquiaEvento","AFECTACION"]]
etiquetas["AFECTACION"].value_counts()
'''


# In[81]:


""""data_entropy_dtw = pd.merge(entropy,dtw,how="inner",on="GeoIdEvento")
data_with_freqs_hour = pd.merge(data_entropy_dtw, freq_sub_hours, how = "inner", on="GeoIdEvento")
data_with_degree = pd.merge(data_with_freqs_hour, degree_difference, how = "inner", on="GeoIdEvento")

df_eventos = pd.read_csv("../eventos.csv", encoding = "ISO-8859-1")
df_eventos = df_eventos[["GeoIdEvento","ParroquiaEvento"]]
df_eventos = df_eventos.drop_duplicates()
data_with_villages = pd.merge(data_with_degree, df_eventos, how = "inner", on="GeoIdEvento")
data_with_tags = pd.merge(data_with_villages, etiquetas, how = "left", on="ParroquiaEvento")
data_with_tags
""""


# In[ ]:


#split in train and test
from sklearn.model_selection import train_test_split

X_train, X_test = train_test_split(data, test_size=0.2, random_state=int(time.time()))
just_features = X_train[:-1]
target = X_train[-1]

#Select best features with PCA
from sklearn.decomposition import PCA

pca = PCA(n_components=3)
principalComponents = pca.fit_transform(just_features) #get PCA without target column

# Dump components relations with features:
print pd.DataFrame(pca.components_,columns=data_scaled.columns,index = ['PC-1','PC-2', 'PC-3'])

#get new dataframe with PCA components
new_df = pd.DataFrame(data = principalComponents, columns = ['PC-1','PC-2', 'PC-3'])




# In[82]:


#Construct and train the model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets 
model.fit(new_df, target)


# In[ ]:


#Test
y_pred = gnb.predict(X_test[:-1])

