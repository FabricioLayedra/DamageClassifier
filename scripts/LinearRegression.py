#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


# In[ ]:


#open dataset
data = 


# In[ ]:


#split in train and test
from sklearn.model_selection import train_test_split

X_train, X_test = train_test_split(data, test_size=0.2, random_state=int(time.time()))
just_features = X_train[:-1]
target = X_train[-1]
y_test = X_test[-1]
X_test = X_test[:-1]


# In[ ]:


# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(just_features, target)

