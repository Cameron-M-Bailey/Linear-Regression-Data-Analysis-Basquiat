#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import cv2
from scipy.misc import face
from numpy.linalg import norm


# In[4]:


#read image file
src = cv2.imread('0_Untitled.jpeg')


# In[6]:


# calculate the average counts of colors
def count_colours(src):
    unique, counts = np.unique(src.reshape(-1, src.shape[-1]), axis=0, return_counts=True)
    return np.mean(counts.size)

count_colours(src)

# Credit: @sazr on Stack Overflow
# https://stackoverflow.com/questions/56606294/count-number-of-unique-colours-in-image


# In[10]:


# read image
img = src

# convert to LAB color space
lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)

# separate channels
L,A,B=cv2.split(lab)

# compute minimum and maximum in 5x5 region using erode and dilate
kernel = np.ones((5,5),np.uint8)
min = cv2.erode(L,kernel,iterations = 1)
max = cv2.dilate(L,kernel,iterations = 1)

# convert min and max to floats
min = min.astype(np.float64) 
max = max.astype(np.float64) 

# compute local contrast
contrast = (max-min)/(max+min)

# get average across whole image
average_contrast = 100*np.mean(contrast)

# return average contrast 
print(str(average_contrast))

# Credit: @fmw42 on Stack Overflow
# https://stackoverflow.com/questions/57256159/how-extract-contrast-level-of-a-photo-opencv


# In[5]:


# calculate average image brightness 
def brightness(img):
    if len(img.shape) == 3:
        
        # Colored RGB or BGR (*Do Not* use HSV images with this function)
        # create brightness with euclidean norm
        return np.average(norm(img, axis=2)) / np.sqrt(3)
    else:
        
        # Grayscale
        return np.average(img)

brightness(src)

# Credit: @AlexLoss on Stack Overflow
# https://stackoverflow.com/questions/14243472/estimate-brightness-of-an-image-opencv

