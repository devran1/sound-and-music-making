#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import wave
import scipy.io.wavfile

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
    

    #for i in range(divided_data):

    for i,j in enumerate(divided_data):    
        print(i,j)
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