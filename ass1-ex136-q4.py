#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import math


# In[141]:


data = [
    28, 22, 23, 20, 12, 24, 37, 28, 21, 25,
    21, 14, 30, 23, 27, 13, 23, 7, 26, 19, 
    24, 22, 26, 3, 21, 24, 28, 40, 27, 24,
    20, 25, 23, 26, 47, 21, 29, 26, 22, 33,
    27, 9, 13, 35, 20, 16, 20, 25, 18, 22
]


# In[170]:


def frequency_distribution(data, nc):
    data = sorted(data)
    lr, hr = get_rounds(data)
    grouped = [[i, [j for j in data if j >= i[0] and j<= i[1]]] for i in gen_classes(nc, lr, hr)]
    classes = [k[0] for k in grouped]
    freq = [len(k[1]) for k in grouped]
    [print(g) for g in grouped]
    fq = [classes, freq]
    return fq
    
def get_rounds(data):
    data = sorted(data)
    lowest_round = round(data[0], -1)
    if lowest_round > data[0]:
        lowest_round = lowest_round - 10
    highest_round = round(data[-1], -1)
    return (lowest_round, highest_round)


def gen_classes(nc, lr, hr):
    bounds = hr - lr
    mid_r = math.floor(bounds/nc)
    class_sizes = [0]
    while sum(class_sizes) != 50:
        class_sizes = [rd.randint(mid_r - 2, mid_r + 2) for i in range(nc)]
    k = []
    curr_ind = 0
    next_ind = 0
    for i in class_sizes:
        next_ind = next_ind + i
        k.append((curr_ind, next_ind))
        curr_ind = next_ind + 1
    print(class_sizes)
    return k
    
fq = frequency_distribution(data, 8)


# In[169]:


pd.DataFrame(fq)


# In[ ]:




