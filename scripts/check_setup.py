import torch
import torchaudio
import numpy

print(torch.__version__)
print(torchaudio.__version__)
print(numpy.__version__)
print(torch.backends.mps.is_available())

t = torch.tensor([1.0, 2.0, 3.0])
print(t)
print(t.shape)
