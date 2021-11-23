#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import wave
import scipy.io.wavfile

file = '2-odum.wav'

with wave.open(file,'r') as wav_file:


    
    
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

    
        
    #print(divided_data)    

    #for i in range(divided_data):

    
    #Plot
    plt.figure(1)
    plt.title('Signal Wave...')
    for channel in channels:
        plt.plot(Time,channel)
    plt.show()