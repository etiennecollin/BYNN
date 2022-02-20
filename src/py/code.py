import torch
import numpy as np
from PIL import Image
from tqdm import tqdm
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
import json
import torch.nn.functional as F

def importTarget(filepath, scale = 0.25, side = 32):
    with open(filepath, "r") as read_file:
        data = json.load(read_file)
    shapes = data.get("shapes")
    target = torch.empty(int(data.get("imageHeight")*scale), int(data.get("imageWidth")*scale))
    for i in range(len(shapes)):
        x_pos = round(shapes[i].get("points")[0][1]*scale)
        y_pos = round(shapes[i].get("points")[0][0]*scale)
        target[x_pos][y_pos] = 1
    target = F.pad(target, pad=(16, 16 ,16 ,16), value=0)
    target_map = torch.empty(1008, 756)
    for i in tqdm(range(1008-side)):
        for j in range(756-side):
            target_map[i][j] = torch.count_nonzero(target[i: i+side, j:j+side])
    
    return target_map

def cellCount(map):
    return torch.sum(map)/(1024)

def importPicture(path):
    img = Image.open(path).convert("L").resize((756, 1008))
    return transforms.ToTensor()(img)