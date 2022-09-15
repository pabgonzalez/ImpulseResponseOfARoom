import scipy
import numpy as np
from matplotlib import pyplot as plt
from playsound import playsound

fs = 48000
n_sec = 10
f = 100
t = np.linspace(start=0, stop=n_sec, num=n_sec*fs)
x = np.iinfo(np.int16).max * scipy.signal.square(2 * np.pi * f * t)
plt.figure(1)
plt.plot(t, x)


scipy.io.wavfile.write("recordings/square_wave.wav", fs, x.astype(np.int16))
#playsound("recordings/square_wave.wav")

rate, data = scipy.io.wavfile.read("mic/square_wave_mic.wav")
data = data[90600:565000]
plt.figure(2)
plt.plot(data[:48000])
plt.title(f"fs={rate} len(data)={len(data)}")
plt.show()