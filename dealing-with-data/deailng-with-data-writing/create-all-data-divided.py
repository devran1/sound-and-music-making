import matplotlib.pyplot as plt
import numpy as np
import wave
import scipy.io.wavfile
import random
import csv
import pandas as pd

#long musics can wait "adele-skyfall-unlogix-remix.wav","apparat-goodbye-dark-netflix-soundtrack-cyantist-remix-progressive-techno.wav","gta-iv-theme-soviet-connection-extended-mix.wav","the-neighbourhood-sweater-weather-gaullin-remix.wav",'yt1s.com - Cryptex  Slay It.wav'


a=["Hope.wav","odum.wav","astral.wav" ,"beggin-madcon-edit-audio.wav","carmine-cassese-dark-dark-netflix-remix-techno.wav","deep-end.wav" ,"ellie-goulding-lights-nitti-gritti-remix.wav" ,"enya-exile-skeler-remix-audio-burial.wav" ,"frxxman-memento.wav" ,"galoski-xtc.wav" ,"grimes-4am-skeler-remix.wav" ,"gta-san-andreas-theme-song-pedrodjdaddy-trap-2021-remix.wav" ,"killka.wav" ,"kslv-disaster-bass-boosted.wav" ,"kslv-d-i-s-a-s-t-e-r-slowed-reverb.wav" ,"last-dawn.wav" ,"lorn-acid-rain.wav" ,"lxst-cxntury-distortion.wav" ,"lxst-cxntury-vega.wav" ,"lxviathxn-impulse.wav" ,"madcon-beggin-abeats-dj-remix.wav" ,"madcon-beggin-elbrus-mirzabekov-remix-new-2019.wav" ,"madcon-beggin-white-remix.wav" ,"meg-dia-monster-dotexe-dubstep-remix.wav",'Nightcore - Giger Effect.wav', "polaris.wav", "radical.wav", "saturn.wav", "smoked-out.wav",'SVARDSTAL - NIGHT DRIVE.wav', "sweater-weather-slowed-reverb-rain.wav",  "v21-cygnus.wav", "v21-proxima.wav",'yt1s.com - 28 days later theme techno remix.wav','yt1s.com - BICEP X NELLY FURTADO  GLUE X SAY IT RIGHT SWITCH DISCO EDIT.wav', 'yt1s.com - Dead Sara  Gimmie Gimme Official Music Video.wav','yt1s.com - Dexter Soundtrack  Die This Way RapHip Hop Remix.wav','yt1s.com - Dido  Thank You  EDM ComBat Remix Rock Lee.wav','yt1s.com - Drift Night.wav','yt1s.com - End of the World Slowed.wav','yt1s.com - Fall Out Boy  Centuries Slowed  Reverb.wav','yt1s.com - Forgottenage  headshot.wav','yt1s.com - FORGOTTENAGE PRXSXNT FXTURE  Triple Six HOUSEDRIFT PHONK ZXC.wav','yt1s.com - impossibleSlowed  Reverb.wav','yt1s.com - Locked Out Of Heaven TikTok Depression RMX.wav','yt1s.com - Offender.wav','yt1s.com - Sheriff.wav','yt1s.com - Slay It Trizity Remix  Cryptex.wav','yt1s.com - Take Me.wav','yt1s.com - The Glitch Mob  Drive it Like You Stole it Cryptex Reglitch.wav','yt1s.com - The Walking Dead Cryptex Reglitch.wav','yt1s.com - valhalla  slowed.wav','yt1s.com - Veorra  Run.wav','[YT2mp3.info] - Danger (320kbps).wav','[YT2mp3.info] - Do To Death (320kbps).wav','[YT2mp3.info] - Exterminator (320kbps).wav','[YT2mp3.info] - FORGOTTENAGE - END OF THE WORLD (320kbps).wav','[YT2mp3.info] - HEAVENLY (320kbps).wav','[YT2mp3.info] - mxnarch - Nightwing (HOUSE_DRIFT PHONK ZXC) (320kbps).wav',"adele-skyfall-unlogix-remix.wav","apparat-goodbye-dark-netflix-soundtrack-cyantist-remix-progressive-techno.wav","gta-iv-theme-soviet-connection-extended-mix.wav","the-neighbourhood-sweater-weather-gaullin-remix.wav",'yt1s.com - Cryptex  Slay It.wav']

#working but if it is big data giving error killing it

#a=["deep-end.wav" ,"ellie-goulding-lights-nitti-gritti-remix.wav" ,"enya-exile-skeler-remix-audio-burial.wav" ,"frxxman-memento.wav" ,"galoski-xtc.wav"]

#a=["deep-end.wav"]

#print(len(a))



#all_original_data=[]
#all_data_for_shuffling=[]

#b=np.array(a).reshape(4,16) #(16,4) #(4,16)
#a,c=b.shape
#print(c)
#for i in b:
#    for m in range(c):
        #print(i[m])

    #print(i[0])
#        pass

for i in a:
    wav_file=wave.open(f"music/{i}","r")
        
    signal =wav_file.readframes(-1)
    signal=np.frombuffer(signal, np.int16)


    channels = [[] for channel in range(wav_file.getnchannels())]
    for index, datum in enumerate(signal):
        channels[index%len(channels)].append(datum)

    #Get time from indices
    fs = wav_file.getframerate()
    
    Time=np.linspace(0, len(signal)/len(channels)/fs, num=int(len(signal)/len(channels)))
    
    divided_data=[]
    for j in range(int(Time[-1])+1):
        j=j+1    
        divided_data += [signal[(j-1)*int(len(signal)/Time[-1]):j*int(len(signal)/Time[-1])]]
        
    with_order=[]
    for k,l in enumerate(divided_data):
        o_data=[k,l]
        with_order +=[o_data]


    #writing the original
    df=pd.DataFrame(with_order)    
    df.to_pickle(f"music-data/original-data/original-{i}-.pickle")
        

    shuffling_data=with_order
    random.shuffle(shuffling_data)

    shuffle_data=[]
    data_for_music=[i for i in shuffling_data]
    #print(data_for_music)
    #writing unordered music data to pickle
    df=pd.DataFrame(data_for_music)    
    #print(dir(df))
    df.to_pickle(f"music-data/shuffled-data/shuffled-{i}-.pickle")
