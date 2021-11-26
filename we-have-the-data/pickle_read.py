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
#print(y[1][0]) y[0][0] y[1][0]

z=pd.read_pickle("original-odum.pickle")
print(z)

t=pd.read_pickle("all-original.pickle")
#print(t)

#s=pd.read_pickle("music-data/original-data/original-astral.wav-.pickle")
#print(s)

#g=pd.read_pickle("music-data/shuffled-data/shuffled-astral.wav-.pickle")
#print(g)