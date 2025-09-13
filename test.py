import torch
print(torch.version.cuda)          # PyTorch 编译时的 CUDA
print(torch.cuda.is_available())   # 是否可用 GPU
