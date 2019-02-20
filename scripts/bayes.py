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


# In[ ]:


data = pd.read_csv("../data/dataset_unificado.csv")


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

