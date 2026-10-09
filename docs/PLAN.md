# Plan

## Working agreement

Each lesson follows the same loop:

1. **Learn.** Concept explained in small pieces: intuition, tiny example, then the formal idea.
2. **Check.** Short questions. Move on only when the idea is clear.
3. **Code.** Smallest piece that makes the idea real. Print shapes, plot, compare with a library reference.
4. **Commit.** One lesson, one commit, with notes in `docs/notes/`.

Rules:
- No code before the concept is understood.
- Overfit one small batch before any real training.
- Every model change gets a WER number.

## Phases

### Phase 0: Setup
- Learn: what the project is, the 3-stage map (features, model, decoding).
- Code: `uv` env, repo layout, git.
- Done when: `uv run python -c "import torch"` works.

### Phase 1: Audio and features
- Learn: sound, sampling, sample rate, frequency, spectrum, why 25 ms windows, mel, log.
- Code: load a wav; plot waveform; FFT of one frame; full spectrogram; mel; compare with torchaudio.
- Done when: your own voice recording shows a clean log-mel plot and you can explain each axis.

### Phase 2: Text side
- Learn: what the model must output; characters vs words vs subwords; WER.
- Code: character tokenizer (text to ids and back); WER with edit distance.
- Done when: WER matches the `jiwer` library on test sentences.

### Phase 3: PyTorch warm-up
- Learn: tensors, layers, loss, optimizer, training loop, overfitting.
- Code: train a tiny classifier on a toy problem.
- Done when: you can read and write a training loop without help. Skip if already comfortable.

### Phase 4: Data
- Learn: LibriSpeech structure; why batches need padding and length tracking.
- Code: download a small subset; `Dataset`; `DataLoader` with a collate function.
- Done when: one batch prints correct shapes: features, feature lengths, targets, target lengths.

### Phase 5: Model (encoder)
- Learn: convolution over time, recurrent layers (GRU/LSTM), why we shrink the frame rate.
- Code: conv subsampling plus BiGRU plus linear layer giving `(frames, vocab)` scores.
- Done when: forward pass runs and output length matches the expected shrink.

### Phase 6: CTC, in small steps
The idea is the hardest in the project, so it gets its own phase, taught gradually.
- 6a. The alignment problem, with a 3-word toy example done by hand. No formulas.
- 6b. Collapse rule and the blank symbol. Code: `collapse(path)`.
- 6c. Count all paths for tiny cases by brute force. Code: enumerate paths, sum probabilities. Reproduce the "0.72" example.
- 6d. Why brute force fails, and how a table (dynamic programming) fixes it. Code: forward algorithm.
- 6e. Compare your loss against `torch.nn.CTCLoss`.
- Done when: your loss matches PyTorch's to 4 decimals.

### Phase 7: Training
- Code: training loop; overfit one batch; then train on about 10 hours of audio; log loss and WER.
- Learn: learning rate, loss plateau at the start (normal), reading curves.
- Done when: WER on a held-out set is clearly below 100% and falling.

### Phase 8: Decoding
- Code: greedy decoder; beam search; optional n-gram language model.
- Done when: beam search beats greedy on WER.

### Phase 9: Improve
- Code: SpecAugment, learning-rate schedule, a bigger or Conformer encoder.
- Done when: a results table shows each change and its WER.

### Phase 10: Service
- Code: FastAPI `POST /transcribe`; then WebSocket streaming; voice activity detection to chunk audio; simple web page with mic.
- Done when: you speak into the browser and see text.

### Phase 11: Compare with Whisper
- Learn: encoder-decoder, attention, why it needs more data.
- Code: run whisper-tiny; compare WER and speed against your model.

## Target repo layout (grows as we go)

```
speech_to_text/
  README.md
  docs/PLAN.md          this file
  docs/notes/           one note per lesson, written by you in your own words
  src/                  library code (features, tokenizer, metrics, data, model, ctc, decode)
  scripts/              runnable entry points (train, evaluate)
  tests/                small checks (WER, collapse, CTC vs PyTorch)
  data/                 ignored by git
```

## Git conventions

- Branch `main`. One short-lived branch per phase, e.g. `phase-1-features`.
- Conventional commits: `feat:`, `docs:`, `test:`, `fix:`.
- Data, checkpoints, and audio files stay out of git.
