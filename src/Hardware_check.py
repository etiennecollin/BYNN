#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
from IPython.display import Image  # for displaying images


# In[2]:


def pytorch_test():
	if torch.cuda.is_available():
		print('torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0)))
		print("\nCUDA available.")
		print(f"\nCurrent CUDA device: {torch.cuda.current_device()}")
		print(f"\nCurrent CUDA device name: {torch.cuda.get_device_name(0)}")
		device = torch.device("cuda:0")
	else:
		print('torch %s %s' % (torch.__version__, "CPU"))
		device = torch.device("cpu")

	x = torch.rand(5, 3).to(device)
	print(f"\nx: {x}")
	print(f"\n x Processed by CUDA: {x.is_cuda}")

	X_train = torch.FloatTensor([0., 1., 2.]).to(device)
	print(f"\nX_Train: {X_train}")
	print(f"\nX_Train Processed by CUDA: {X_train.is_cuda}")
    
if __name__ == '__main__':
	pytorch_test()


# In[ ]:




