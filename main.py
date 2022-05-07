# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import numpy as np

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
print('Finished recording')

plt.plot(myrecording)
plt.ylabel('Sound')
plt.xlabel('Time')
plt.show()

signal = myrecording
fourier = np.fft.fft(signal)
n = signal.size
timestep = 0.1
freq = np.fft.fftfreq(n, d=timestep)
print(freq)

sd.play(myrecording, fs)
sd.wait()
print('Finished playing')