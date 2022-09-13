---
layout: default
title: The Prerequisites
nav_order: 3
description:
---

# The Prerequisites

This section will guide you through installing the various prerequisites of the BYNN project.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Python

First, let's install Python. Python is the programming language we are going to use throughout this tutorial and is widely used in the scientific community for its various and incredibly useful packages. Although Python is pre-installed on many systems, this pre-installed version is often outdated. Hence, we will install a more recent version. The simplest way to do so is by going to the [Python.org download page](https://www.python.org/downloads/) to download the latest version. You may click the following link and follow the install process for your OS (Operating System):

```
https://www.python.org/downloads/
```

## Anaconda & Conda

We will install the necessary packages for our project in a compartmentalized **conda** environment using **Anaconda**. This makes it easy to keep track of the packages we install and keep them at a specific version. It also allows us to use a specific Python version for our project; certain Python packages are not yet compatible with the most recent versions of Python.

To install Anaconda (and conda), you may click the following link and follow the install process based on your OS:

```
https://docs.anaconda.com/anaconda/install/
```

## Virtual Environment

Once Anaconda is installed, we will create an environment for the BYNN project. The following command creates the environment using conda[^condasupport]:

```
conda create -n <name> python=<version>
```

The argument `<name>` specifies the name of the environment and the `<version>` tag specifies the version of Python we wish to use.

We will create one with the name "BYNN" and the latest 3.9.x Python version as it is the latest version compatible with the packages we will use as of now.

```
conda create -n BYNN python=3.9
```

Before continuing, let's activate the environment:

```
conda activate <name>
```

where `<name>` is the name you specified using the `-n` flag when creating the environment. If you followed the tutorial, the command should be:

```
conda activate BYNN
```

**IMPORTANT: For the rest of the tutorial, and of your project, the conda environment you created should be activated.**

## YOLOv5

With the conda environment activated, run the following commands to download the YOLOv5 project from github and install its requirements[^yolov5support]:

```
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```

The first line will clone (download) the github repository of the project on your computer. The second one will move you inside the folder you just downloaded. The third line will install the requirements for the YOLOv5 project.

## Labelling/Annotation

Similarly to children, computers have to learn what an object is to gain the ability to identify it in any environment. In the case of this tutorial, that means teaching the computer what a cell in each stage of mitosis looks like. That is, we need to provide _ground truth_ to our neural network so that it knows what each cell should look like. In another project, ground truth could be what a dog looks like versus a cat.

This teaching will be achieved through the annotation of images. Put simply, with a computer, we will have to manually identify the objects we wish to detect with the neural network. Two tools to identify the objects are presented here. Both of them are simple and free to use which is why they were chosen amongst others. The first one, Roboflow, is an online platform that allows the user to label objects on their images and format their labels. The second one, LabelMe, is an open-source software that is downloaded and may be used offline. That said, LabelMe requires some tinkering to get the labels in the right format and does not provide the ability to perform other actions on the dataset. This is why, although LabelMe could be used to follow this tutorial, Roboflow will be used for its simplicity of use. A link to LabelMe will still be provided.

### Roboflow

### LabelMe

---

[^condasupport]: All of the information provided in this subsection is taken from the official [conda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
[^yolov5support]: All of the information provided in this subsection is taken from the official [YOLOv5 README](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
