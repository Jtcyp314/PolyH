import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import numpy as np

def get_note(data):
    c = fft(data)
    note = (abs(c).tolist().index(max(abs(c).tolist())))/3
    return note

def seperate_notes(whole_recording, threshold):
    seperated_notes=[]
    j = 0
    for i in range(int(len(data)/10)-100):
        if sum(abs(whole_recording[i*10:i*10+100])) < threshold:
            single_note = whole_recording[j*10:i*10]
            seperated_notes.append(single_note)
            j = i
    single_note = whole_recording[j*10:i*10]
    seperated_notes.append(single_note)
    return(seperated_notes)

def get_time(seperated_note, fs):
    time_in_sec = len(seperated_note)/fs
    return(time_in_sec)

fs, data = wavfile.read('300Hz.wav') # load the data
notes = seperate_notes(data, 10)
print(len(notes))
freq_and_time = []
for k in range(len(notes)):
    freq_and_time.append([get_note(notes[k]), get_time(notes[k],fs)])
print(freq_and_time)