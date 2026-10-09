# 1.2 One sound is many frequencies

## Real sounds are mixtures
Speech, music and chords are not one clean sine wave. They are many sine waves added together. The sum looks like a lumpy curve, and you cannot read the individual frequencies off it by eye.

## Fourier idea
Any waveform equals a sum of sine waves, each with its own frequency and strength. The **FFT** (fast Fourier transform) computes, for each frequency, how strong it is. The result is a **spectrum**: frequency on the x axis, strength on the y axis.

Example: 440 Hz + 0.5 * 880 Hz gives a messy waveform but a spectrum with two spikes, at 440 Hz (height 1) and 880 Hz (height half as big).

A spectrogram is this same idea repeated on short time slices. That is why this lesson comes before spectrograms.

## NumPy tools

```python
spectrum = np.fft.rfft(audio)                         # one complex number per frequency
strength = np.abs(spectrum)                           # magnitude; ignore phase for now
freqs = np.fft.rfftfreq(len(audio), d=1/sample_rate)  # frequency in Hz of each value
```

- `rfft` is the version for real-valued signals like audio. It returns frequencies from 0 up to Nyquist.
- Phase (the other half of the complex number) is dropped. For recognizing speech, which frequencies are present matters far more.

## Resolution preview
Spacing between frequency values is `sample_rate / len(audio)` Hz, i.e. `1 / duration`.

- 1 second of audio: 1 Hz spacing.
- 25 ms of audio: 40 Hz spacing.

Shorter slices see time more precisely but frequency more coarsely. This trade-off decides the window size when we build spectrograms.

## Aliasing in the spectrum
A tone above Nyquist shows up as a spike at the alias frequency instead of its true one (see note 1.1).

## Task
`scripts/lesson1_spectrum.py`: mix 440 Hz and 0.5 * 880 Hz, plot the waveform and the spectrum, print the strongest frequency. Then repeat with 5000 Hz at 8 kHz sampling and find where the spike lands.
