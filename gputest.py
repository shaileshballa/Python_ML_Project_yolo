import torch
print(torch.__version__)
print(torch.cuda.is_available())  # Should return True
print(torch.version.cuda)  # Should return 12.1 or 12.x
print(torch.cuda.get_device_name(0))  # Should return RTX 3050
