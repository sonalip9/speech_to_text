# 1.1 Sound becomes numbers

## Sound is a pressure wave
A vibrating source (speaker cone, vocal cords) squeezes and thins the air. Plotting the pressure at one point over time gives a smooth curve called a **waveform**. A microphone turns that pressure into a voltage with the same shape.

## Sampling
A smooth curve has infinitely many points, and memory is finite. So we **sample**: measure the value at regular intervals and keep only those numbers.

- **Sample**: one measurement, a single number.
- **Sample rate**: measurements per second, in Hz. ASR uses 16,000 Hz.

## Audio is an array
One second at 16 kHz is 16,000 numbers. Values lie roughly in [-1, 1]; 0 is silence, larger magnitude is louder.

```
num_samples = duration_seconds * sample_rate
duration_seconds = num_samples / sample_rate
```

Same sound at a lower sample rate gives a shorter array: 2 s at 16 kHz is 32,000 samples; at 8 kHz it is 16,000.

## Nyquist limit
To capture a wiggle you need at least two samples per up-down cycle. So the highest frequency a sample rate can represent is:

```
nyquist = sample_rate / 2
```

- 16 kHz sampling: up to 8 kHz. Enough for speech.
- 8 kHz sampling (phone calls): up to 4 kHz.

## Aliasing
A tone above Nyquist cannot be stored. It folds back below the limit and becomes a different, lower tone: `alias = sample_rate - freq`.

Measured in the experiment: a 5000 Hz sine sampled at 8000 Hz produces a 3000 Hz tone (8000 - 5000). Two different real sounds map to the same array, and the information is lost for good.

Consequence for ASR: always resample to 16 kHz with a proper resampler that low-pass filters first. Keeping every other sample aliases high frequencies into the speech band.

## Time axis in code

```python
t = np.arange(num_samples) / sample_rate      # sample n happens at n / sample_rate seconds
audio = np.sin(2 * np.pi * freq * t)          # pure tone of `freq` cycles per second
```

## Mistakes to remember
- Resampling 16 kHz to 8 kHz halves the sample count (does not double it).
- Nyquist is half the sample rate, not the sample rate.

## Code
`scripts/lesson1_sine.py`: generates a sine tone, plots the first 100 samples, writes a wav file.
