#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import wave
import scipy.io.wavfile
import random
import csv
import pandas as pd


file = 'odum.wav'

#music files were 2 seconds,and really works just make wav to mp3 and then play

with wave.open(file,'r') as wav_file:


    #print(wav_file.getnchannels())
    nchannels=wav_file.getnchannels()
    frame_rate=wav_file.getframerate()
    frames = wav_file.getnframes()
    sampwidth=wav_file.getsampwidth()
    #print(dir(wav_file))

    #Extract Raw Audio from Wav File
    signal = wav_file.readframes(-1)
    #print("first",signal)
    #signal=signal[:10]
    signal = np.fromstring(signal, np.int16)
    #print("second",signal)
    #print(len(signal))
    
    #Split the data into channels 
    channels = [[] for channel in range(wav_file.getnchannels())]
    for index, datum in enumerate(signal):
        channels[index%len(channels)].append(datum)

    #Get time from indices
    fs = wav_file.getframerate()
    
    Time=np.linspace(0, len(signal)/len(channels)/fs, num=int(len(signal)/len(channels)))
    
    #print(Time[-1])

    #print(len(signal)/Time[-1])

    #print(range(int(Time[-1]))) #0-132
    
    divided_data=[]
    #divided_data += [signal[:int(len(signal)/Time[-1])]]
    for i in range(int(Time[-1])+1):
        #print(i)
        i=i+1
        #divided_data += [signal[:int(len(signal)/Time[-1])]]
       
        #print(signal[(i-1)*int(len(signal)/Time[-1]):i*int(len(signal)/Time[-1])])

        divided_data += [signal[(i-1)*int(len(signal)/Time[-1]):i*int(len(signal)/Time[-1])]]
        
        #when even doesnt work,odd works,divided_data[1]=empty???
        #pass
        
    #print(divided_data)
    #d_data=[i for i in divided_data]
    #print(d_data[0])
    #print(d_data[121])

    #unordered data for ai

    with_order=[]
    for i,j in enumerate(divided_data):
        o_data=[i,j]
        with_order +=[o_data]
    #print(with_order)
    data_for_shuffling=[i for i in with_order]

    original_data=data_for_shuffling

    df=pd.DataFrame(original_data)    
    df.to_pickle("original.pickle")
    
    #print("data0",data_for_shuffling[0])
    #print("data131",data_for_shuffling[131])
    

    #shuffling_data=divided_data
    #shuffling_data=random.shuffle(shuffling_data)
    #random.shuffle(shuffling_data)

    shuffling_data=data_for_shuffling
    random.shuffle(shuffling_data)



    shuffle_data=[]
    data_for_music=[i for i in shuffling_data]
    
    #writing unordered music data to pickle

    df=pd.DataFrame(data_for_music)    
    #print(dir(df))
    df.to_pickle("shuffled.pickle")
    









    #shuffle_tuple = []
    for i,j in enumerate(shuffling_data):
        #print(i,j)
    #    data=[i,j]
    #    shuffle_tuple += data
        #data={}
        #df=pd.DataFrame(data)
        #i=[j]
        #df[f"{i}"]=j
        #df.to_csv("shuffling_data.csv")

        #csv_data=open("shuffled_data","w")
        #writer=csv.writer(csv_data)
        #writer.writerow([j])
        #csv_data.close()
        
        #df=pd.DataFrame({f"{i}":j})

        #df.to_csv("shuffling_data.csv",index=False)
        pass
    #df=pd.DataFrame(shuffle_tuple)    
    #df.to_csv("shuffle.txt")

    #for i in range(divided_data):

    
    
    #ordered data
    #ordered for adding as last element with i and j as one list
    for i,j in enumerate(divided_data):    
        #print(i,j)
       
        #pass

        #pass
        #music_part=wave.open(f"{file}-{i}.wav","w")
        #scipy.io.wavfile.write(f"{file}-{i}.wav",frame_rate,j)
        
        #scipy.io.wavfile.write(f"{i}-{file}",frame_rate,j)
        
        #music_part.write(j)
        pass

    
    #Plot
    plt.figure(1)
    plt.title('Signal Wave...')
    for channel in channels:
        plt.plot(Time,channel)
    #plt.show()