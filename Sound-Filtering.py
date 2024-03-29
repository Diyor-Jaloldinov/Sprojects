


import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write     # Imported libaries such as numpy, scipy(read, write), matplotlib.pyplot
from scipy import signal
import matplotlib.pyplot as plt


(Frequency, array) = read('eagle.wav') # Reading the sound file. 



len(array) # length of our array





plt.plot(array) 
plt.title('Original Signal Spectrum')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')





FourierTransformation = sp.fft(array) # Calculating the fourier transformation of the signal





scale = sp.linspace(0, Frequency, len(array))





plt.stem(scale[0:5000], np.abs(FourierTransformation[0:5000]), 'r')  # The size of our diagram
plt.title('Signal spectrum after FFT')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')




GaussianNoise = np.random.rand(len(FourierTransformation)) # Adding guassian Noise to the signal.

plt.plot(GaussianNoise) # plotting the GuassianNoise.
plt.title('GaussianNoise+Signal spectrum after FFT')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')


NewSound = GaussianNoise + array




write("New-Sound-Added-With-Guassian-Noise.wav", Frequency, NewSound) # Saving it to the file.




b,a = signal.butter(5, 1000/(Frequency/2), btype='highpass') # ButterWorth filter 4350




filteredSignal = signal.lfilter(b,a,NewSound)
plt.plot(filteredSignal) # plotting the signal.
plt.title('Highpass Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')




c,d = signal.butter(5, 380/(Frequency/2), btype='lowpass') # ButterWorth low-filter
newFilteredSignal = signal.lfilter(c,d,filteredSignal) # Applying the filter to the signal
plt.plot(newFilteredSignal) # plotting the signal.
plt.title('Lowpass Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')




write("New-Filtered-Eagle-Sound.wav", Frequency, newFilteredSignal) # Saving it to the file.
print("its been done please check the file Sound-Filtering.py is in ")
