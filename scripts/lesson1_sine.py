import numpy as np
import soundfile
import matplotlib.pyplot as plt

sample_rate = 8000
duration = 1.0
freq = 440

num_samples = int(sample_rate * duration)
t = np.arange(num_samples) / sample_rate
audio = np.sin(2 * np.pi * freq * t)

print(audio.shape)
print(len(audio) / sample_rate)
print(audio[:5])

plt.figure()
plt.plot(t[:100], audio[:100], "o-")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title(f"{freq} Hz Sine Wave")
plt.savefig(f"outputs/{freq}_Hz_{sample_rate}_Hz_sine_wave.png")


path = f"outputs/{freq}_Hz_{sample_rate}_Hz_sine_wave.wav"
soundfile.write(path, audio, sample_rate)
