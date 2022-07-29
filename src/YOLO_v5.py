#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('git clone https://github.com/ultralytics/yolov5  # clone repo')
get_ipython().system('pip install -U -r yolov5/requirements.txt  # install dependencies')

get_ipython().run_line_magic('cd', '~/GitHub/BYNN/src/yolov5')


# In[ ]:


import torch
from IPython.display import Image  # for displaying images


# In[ ]:


import torch
torch.cuda.empty_cache()

get_ipython().run_line_magic('cd', '~/GitHub/BYNN/src/yolov5')

get_ipython().system("python train.py --img 640 --batch 4 --epochs 300 --data dataset/data.yaml --cfg ./models/custom_yolov5x.yaml --weights '' --name yolov5x_results  --cache")


# In[ ]:


# Start tensorboard
# Launch after you have started training
# logs save in the folder "runs"
get_ipython().run_line_magic('cd', '~/GitHub/BYNN/src/yolov5')
get_ipython().run_line_magic('load_ext', 'tensorboard')
get_ipython().run_line_magic('tensorboard', '--logdir runs')


# In[ ]:


get_ipython().run_line_magic('cd', '~/GitHub/BYNN/src/yolov5')

get_ipython().system('python detect.py --weights runs/train/yolov5x_results/weights/best.pt --img 640 --conf 0.15 --source dataset/test/images')


# In[ ]:


import glob
from IPython.display import Image, display

get_ipython().run_line_magic('cd', '~/GitHub/BYNN/src/yolov5')

for imageName in glob.glob('runs/detect/exp/*.jpg'): #assuming JPG
    display(Image(filename=imageName))
    print("\n")


# In[ ]:


# optional, zip to download weights and results locally

get_ipython().system('zip -r export.zip runs/detect')
get_ipython().system('zip -r export.zip runs/train/BYNN/weights/best.pt')
get_ipython().system('zip export.zip runs/train/BYNN/*')

