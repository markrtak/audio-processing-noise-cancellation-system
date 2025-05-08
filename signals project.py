import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft, ifft

t = np.linspace(0, 3, 3 * 44100 )
x = np.zeros(t.shape)  
N=3
notepairs = []
octave_3 = [130.81, 146.83, 164.81, 174.61, 196.00, 220.00, 246.94]  
octave_4 = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
Fi = {'C': 130.81, 'D': 146.83, 'E': 164.81, 'F': 174.61, 'G': 196.00, 'A': 220.00, 'B': 246.94}
fi = {'C': 261.63, 'D': 293.66, 'E': 329.63, 'F': 349.23, 'G': 392.00, 'A': 440.00, 'B': 493.88}
notes = ['C', 'D', 'E']
#Fi = np.random.choice(octave_4)
#fi = np.random.choice(octave_3)

ti = [0,1,2]
Ti = [1,1,1]

#x = np.reshape([t>=0],np.shape(t))
#x_shift = np.reshape([t>=2],np.shape(t))

xOriginal = 0
for j in range(N):
    note = notes[j]
    xOriginal += ((np.sin(2 * np.pi * Fi[note] * t) + np.sin(2 * np.pi * fi[note] * t)) *
           ((t >= ti[j]).astype(float) - (t >= (ti[j] + Ti[j])).astype(float)))

N1 = 3 * 44100
f = np.linspace(0, 512, int(N1/2))
fn1, fn2 = np.random.randint(0, 512, 2)
xOriginalFreq = fft(xOriginal)
xOriginalFreq = 2/N1 * np.abs(xOriginalFreq[0:int(N1/2)])
noise = np.sin(2*np.pi*fn1*t) + np.sin(2*np.pi*fn2*t)
xNoise = xOriginal + noise
xNoiseFreq = fft(xNoise)
xNoiseFreq = 2/N1 * np.abs(xNoiseFreq[0:int(N1/2)])


xFilteredFreq =fft(xNoise)
index_fn1 = int(fn1 * 3)
index_fn2 = int(fn2 * 3) 
index_fn1_neg = N1 - index_fn1 
index_fn2_neg = N1 - index_fn2 


Fs = 44100
index_fn1 = int(fn1 * N1 / Fs)
index_fn2 = int(fn2 * N1 / Fs)
index_fn1_neg = N1 - index_fn1
index_fn2_neg = N1 - index_fn2

xFilteredFreq[index_fn1] = 0
xFilteredFreq[index_fn2] = 0
xFilteredFreq[index_fn1_neg] = 0
xFilteredFreq[index_fn2_neg] = 0

xFiltered = np.real(ifft(xFilteredFreq))
x_f_filtered_mag = 2/N1 * np.abs(xFilteredFreq[0:int(N1/2)])
#xNew = np.subtract(xNew, fn2)



# Plot & play the original signal in time domain
plt.figure()
plt.plot(t, xOriginal)
plt.title("Original Generated Sound Signal")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()
sd.play(xOriginal, 3*44100)
sd.wait()

# Plot the original signal in frequency domain
plt.figure()
plt.plot(f, xOriginalFreq)
plt.title("Original Generated Sound Signal")
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.show()

# Plot and play the original signal with noise in time domain
plt.plot(t,xNoise)
plt.title("Sound Signal with Noise")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()
sd.play(xNoise, 3*44100)
sd.wait()

# Plot the original signal with noise in frequency domain
plt.plot(f,xNoiseFreq)
plt.title("Sound Signal with Noise")
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.show()

# Plot and play the sound signal after noise cancellation in time domain
plt.plot(t,xFiltered)
plt.title("Sound Signal after Noise Cancellation")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()
sd.play(xFiltered, 3*44100)
sd.wait()

# Plot the sound signal after noise cancellation in time domain
plt.plot(f,x_f_filtered_mag)
plt.title("Sound Signal after Noise Cancellation")
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.show()

