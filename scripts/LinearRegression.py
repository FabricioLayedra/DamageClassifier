#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import metrics
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn import svm


# In[60]:


RANDOM_STATE = 42
#open dataset
data = pd.read_csv("../data/dataset_unificado_incompleto.csv")
target = pd.read_csv("../data/labels_incomplete.csv")
target = target[["Parroquia","damage_ratio"]]
data = data.set_index("Parroquia")
target = target.set_index("Parroquia")
data


# In[61]:


#split in train and test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test= train_test_split(data, target, test_size=0.2, random_state=RANDOM_STATE)


# In[62]:


#scale
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# In[63]:


#PCA
pca = PCA(n_components=5)
pca.fit(X_train)
X_train = pca.transform(X_train) 
X_test = pca.transform(X_test)


# In[64]:


'''

pipe = Pipeline([('scaling', StandardScaler()),
                     ('pca', PCA(n_components=5)),
                      ('regr',linear_model.LinearRegression())])
pipe = pipe.fit(X_train, y_train)
print('Testing score: ', pipe.score(X_test, y_test))

'''


# In[65]:


import statsmodels.api as sm
X = sm.add_constant(X_train)
model = sm.OLS(y_train, X).fit()

predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
model.summary()


# In[66]:


lm = linear_model.LinearRegression()
model = lm.fit(X_train,y_train)
lm.score(X_train,y_train)


# In[67]:


y_pred = model.predict(X_test)
y_test.values


# In[68]:


y_pred

