import numpy as np
import matplotlib.pyplot as plt

sample_rate = 16000
duration = 1.0
num_samples = int(sample_rate * duration)
t = np.arange(num_samples) / sample_rate
audio = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)


plt.figure()
plt.plot(t[:400], audio[:400], "o-")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Mixed Wave")
plt.savefig("outputs/mixed_wave.png")

strength = np.abs(np.fft.rfft(audio))
freqs = np.fft.rfftfreq(len(audio), 1 / sample_rate)

plt.figure()
plt.plot(freqs, strength)
plt.xlim(0, sample_rate / 2)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Strength")
plt.title("Mixed Spectrum")
plt.savefig("outputs/mixed_spectrum.png")

print("Frequency with largest strength:", freqs[np.argmax(strength)])
print(np.argsort(strength)[-2:])
print(
    strength[np.argmin(np.abs(freqs - 440))] / strength[np.argmin(np.abs(freqs - 880))]
)
