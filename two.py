import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, rfft, rfftfreq
import numpy as np

fs = 44100  # Sample rate
seconds = 2  # Duration of recording
N = int(fs * seconds)


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


print('Start recording')
myrecording = sd.rec(N, samplerate=fs, channels=1)
sd.wait()
print('Finished recording')
# x, myrecording = generate_sine_wave(400, fs, seconds)


plt.plot(myrecording)
plt.ylabel('Sound')
plt.show()

yf = rfft(myrecording, axis=0)
xf = rfftfreq(N + 1, 1 / fs)
plt.plot(xf[:2000], np.abs(yf)[:2000])
plt.show()

# yf = rfft(myrecording)
# xf = rfftfreq(int(seconds * fs), 1 / fs)
# plt.plot(np.abs(yf))
# plt.show()

sd.play(myrecording, fs)
sd.wait()
print('Finished playing')