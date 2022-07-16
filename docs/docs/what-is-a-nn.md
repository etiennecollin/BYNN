---
layout: default
title: What is a Neural Network?
nav_order: 2
description:
permalink: /what-is-a-nn
---

# What is a Neural Network?

{: .no_toc .text-delta }

-   TOC
    {:toc}

---

## Artificial Intelligence?

Artificial intelligence describes the field where computers are programmed to learn and that neural network are a subfield of the former. In fact, in contrast to traditional programming where a computer is instructed what to do with a specific input, in artificial intelligence, the computer is instructed to learn the relationship between an input and an expected output. Eventually, the computer is able to interpret an input it has never seen before and give an output.

## Objects

Objects are what is being analyzed by the neural network. In our case, a neural network will be used to identify the mitosis stage of multiple cells in a picture; the cells are the objects.

## Example

Here is a very simplified example of how a neural network that identifies cats and dogs as objects is trained[^concept]:

1. The computer is presented with a series of dog images and a series of cat images.
2. Cats and dogs are labeled on each image
3. The computer learns what constitutes a dog and a cat in terms of numbers by analyzing the images
    - Imagine each image as black and white, and as being constituted of pixels each with a value between 0 and 1; 0 is black and 1 is white.[^bw] The computer, in a way, tries to determine what arrangement of numerical values constitues a dog versus a cat.
4. Once trained, the computer should be able to identify a dog or a cat in a picture even if the latter has never been seen before by the computer.

[^concept]: The same concepts will be applied in the BYNN tutorial. The difference with the example is that, in this tutorial, each picture will contain multiple objects.
[^bw]: This will be important further in the tutorial
