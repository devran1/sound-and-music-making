#!/usr/bin/env python3


import pickle
import pandas as pd

#shuffled rigth? not shuffle
#f=open("shuffled.pickle","rb")
#x=pickle.load(f)
#print(x)

#y=pd.read_pickle("shuffle.pickle")
#print(y)

y=pd.read_pickle("shuffled-odum.pickle")
print(y)
z=pd.read_pickle("original-odum.pickle")
print(z)