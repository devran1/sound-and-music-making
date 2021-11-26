#!/usr/bin/env python3
import pickle
import pandas as pd
from pandas.core.arrays.sparse import dtype
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor


import matplotlib.pyplot as plt

import numpy as np


#data=pd.read_pickle(f"music-data/direct-writing/original-data/{i}")

#this is y
#y_data=pd.read_pickle("music-data/direct-writing/original-data/original-adele-skyfall-unlogix-remix.wav-.pickle")

#y_data=pd.read_pickle("music-data/direct-writing/original-data/original-adele-skyfall-unlogix-remix.wav-.pickle")

y_data=pd.read_pickle("one-data/original-Hope.wav-.pickle")


#print(y_data)

#y_data=pd.read_pickle("music-data/direct-writing/original-odum.pickle")
#print(y_data[0])
#print(y_data[1])

#y_flattened= [i for i in y_data[1]]

#flattened=[i for i in y_data]
#print(flattened)

#print(y_data)

#y=list(y_data)
#y=y_data.to_numeric()

#y=y_data.to_numpy()
#y.reshape(-1)


#y=list(y)

#x_data=pd.read_pickle("music-data/direct-writing/shuffled-data/shuffled-adele-skyfall-unlogix-remix.wav-.pickle")

#x_data=pd.read_pickle("music-data/direct-writing/shuffled-data/shuffled-adele-skyfall-unlogix-remix.wav-.pickle")

#x_data=pd.read_pickle("music-data/direct-writing/shuffled-data/shuffled-apparat-goodbye-dark-netflix-soundtrack-cyantist-remix-progressive-techno.wav-.pickle")

x_data=pd.read_pickle("one-data/shuffled-Hope.wav-.pickle")
#print(x_data)
#x_data=pd.read_pickle("music-data/direct-writing/shuffled-odum.pickle")

#x_data=x_data.to_csv("x_data.csv")

#x_flattened= [i for i in list(x_data[1])]
#x_x_flattened=[i for i in list(x_flattened)]

#print(x_x_flattened[0])

#print(type(x_flattened))
#print(x_flattened)

#print(type(x_data))
#x=np.array(x_data)
#x=x_data.to_numpy()

#x=list(x_data)

#x=x_data.to_numeric()

#x=x_data.to_numpy()
#x.reshape(-1)

#x=list(x)



#x0=x_data[0]
#print(x0)
#x1=list(x_data[1])
#np.array(x1, dtype=object)
#print(x1)
#x=zip(x0,x1)
#for i in x:
#    print(i)
#print(x)
#x=[i for i in zip(x0,x1)]
#print(x)
#y1=list(y_data[1])
#print(type(y1))
#print(x)
#print(type(x))


x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=42)



#print(x_train)
#print(x_test)
#print(y_train)
#print(y_test)



lr = LinearRegression()
lr.fit(x_train, y_train)

#print(lr)

#make predictions on the training set and test set as follows:

y_lr_train_pred = lr.predict(x_train)

#list1=[]
#for i in y_lr_train_pred:
#    list1 += i

y_lr_test_pred = lr.predict(x_test)

#all_list=[y_lr_test_pred]+[y_lr_train_pred]
#print(all_list)

#pred_list=[]
#for i in y_lr_test_pred:
#    print(i)
#    pred_list += i
#for j in y_lr_train_pred:
#    pred_list += j

#print(pred_list)


#print(y_lr_train_pred)
#print(y_lr_test_pred)

#determine the model performance.

lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
#print(lr_train_mse)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)
#print(lr_train_r2)


lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
#print(lr_test_mse)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)
#print(lr_test_r2)

"""
#build an RF model using the following code
rf = RandomForestRegressor(max_depth=2, random_state=42)
rf.fit(x_train, y_train)

y_rf_train_pred = rf.predict(x_train)
y_rf_test_pred = rf.predict(x_test)

print(y_rf_train_pred)
print(y_rf_test_pred)
"""