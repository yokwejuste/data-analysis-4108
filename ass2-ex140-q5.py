#!/usr/bin/env python
# coding: utf-8

# In[51]:


import math
k_round(10.4)


# In[133]:


def k_round(num):
    if(round(num%1,1) < 0.5):
        return math.floor(num)
    else:
        return math.ceil(num)
def deciles(data):
    data = sorted(data)
    n = len(data)
    
    # calculates the decile values positions
    di_pos = [(n+1)*(i/10) for i in range(9)]
    di = []
    print(di_pos)
    for pos in di_pos:
        lower = data[math.floor(pos)]
        higher = data[math.floor(pos)]
        
        prec = round(pos%1, 1)
        di.append(lower + (prec * (higher-lower)))
    
    return (di, di_pos)

def decile_groups(data):
    data = sorted(data)
    di_pos = [int(round(p)) for p in deciles(data)[1]]
    
    groups = []
    i = 0
    k = len(di_pos)
    print(di_pos)
    while i < k:
        if i == k-1:
            di_group = data[di_pos[i]:]
        else:
            di_group = data[di_pos[i]:di_pos[i+1]]
        groups.append(tuple(di_group))
        i += 1
    print(data)
    return groups
        


# In[134]:


def median(data):
    data = sorted(data)
    n = len(data)
    mid = 0
    if n % 2 == 0:
        mid = (data[int((n-1)/2)] + data[int((n+1)/2)])/2
    else:
        mid = data[int((n-1)/2)]
    return mid


# In[135]:


def quartile_groups(data):
    data = sorted(data)
    n = len(data)
    q1 = data[int((n+1)/4)]
    q2 = median(data)
    q3 = data[int(3*(n+1)/4)]
    return (q1,q2,q3)
    


# In[136]:


dat = [43,47,30,25,15,51,17,21,37,33,44,56,40,49,22,36,44,33,17,35,58,51,35,44,40,31,41,55,50,16]
dat2 = [40,46,28,32,37,42,50,31,48,45,32,38,27,33,40,35,25,42,38,41]


# In[137]:


decile_groups(dat)


# In[132]:


import pandas as pd
import numpy as np
dat2_df = pd.DataFrame(sorted(dat), columns=['data'])
dat2_df['decile rank'] = pd.qcut(dat2_df['data'],q=10)
dat2_df


# In[ ]:




