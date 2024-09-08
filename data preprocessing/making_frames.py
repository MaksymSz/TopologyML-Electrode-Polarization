#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pickle
import os
import pandas as pd
import numpy as np
import warnings
import random

VERSION = 3
rs = 69
c_set = [3]
p_set = [1]
res_set = [50]
train_size = 400
test_size = 100
namespath = f'C:\\Users\\szeme\\PycharmProjects\\tutoring\\data\\3d_neumann_v{VERSION}\\'

try:
    os.makedirs(f'../data/3d_frames/v_{VERSION}', exist_ok=False)
    print('Directory created')
except Exception as e:
    print('Error creating directory: {}'.format(e))

with open(f'sofc_3d_valid_names_v{VERSION}.pkl', 'rb') as fb:
    names = pickle.load(fb)

# In[48]:

SET_NAME = f'__{train_size}__only_b'
META_N = 3
TEMPERATURE = '800'
names_list = list(names)

# In[50]:

warnings.simplefilter(action='ignore', category=FutureWarning)
random.Random(rs).shuffle(names_list)

# ## train set
# In[55]:

current_density = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 0.0]

idx_names = []
for sofc_name in names_list[test_size:test_size + train_size]:
    file = pd.read_csv(f'{namespath + sofc_name}_{TEMPERATURE}_3d.csv', header=None)
    for i in range(8):
        idx = f'{sofc_name}_{current_density[i]}'
        idx_names.append(idx)

# In[56]:
for C in c_set:
    for p in p_set:
        for res in res_set:
            datapath = f'../data/pi/{res}'
            data = pd.DataFrame(columns=np.arange(res ** 2 * META_N + 1), index=idx_names, dtype='float64')
            target = pd.Series(index=idx_names)
            dataset = f'{res}_005Kusano{C}-{p}{SET_NAME}'
            for sofc_name in names_list[test_size:test_size + train_size]:
                file = pd.read_csv(f'{namespath + sofc_name}_{TEMPERATURE}_3d.csv', header=None)
                for i in range(8):
                    idx = f'{sofc_name}_{current_density[i]}'
                    _rows = []
                    for k in range(3):
                        for phase in ['a', 'b', 'c']:  # <--- changes no 'a'
                            tmp = np.load(f'{datapath}/{res}_005Kusano{C}-{p}/{k}/{phase}/{sofc_name}.npy')
                            _rows.append(tmp)

                    data.loc[idx, 0] = current_density[i]
                    for j in range(0, META_N):
                        data.loc[idx][res ** 2 * j + 1:res ** 2 * j + res ** 2 + 1] = _rows[j]
                    if 7 == i:
                        target.loc[idx] = 0.0
                    else:
                        target.loc[idx] = file.iloc[i, 1]
            data.to_pickle(f'../data/3d_frames/v_{VERSION}/{dataset}_data_train.pkl')
            target.to_pickle(f'../data/3d_frames/v_{VERSION}/{dataset}_target_train.pkl')

## test

# In[58]:

train_idx = target.index.copy()

idx_names = []
for sofc_name in names_list[:test_size]:
    file = pd.read_csv(f'{namespath + sofc_name}_{TEMPERATURE}_3d.csv', header=None)
    for i in range(8):
        idx = f'{sofc_name}_{current_density[i]}'
        idx_names.append(idx)

# In[61]:
test_names = names_list[:test_size]
# In[62]:


for C in c_set:
    for p in p_set:
        for res in res_set:
            datapath = f'../data/pi/{res}'
            data = pd.DataFrame(columns=np.arange(res ** 2 * META_N + 1), index=idx_names, dtype='float64')
            target = pd.Series(index=idx_names)
            dataset = f'{res}_005Kusano{C}-{p}{SET_NAME}'
            for sofc_name in test_names:
                file = pd.read_csv(f'{namespath + sofc_name}_{TEMPERATURE}_3d.csv', header=None)
                for i in range(8):
                    idx = f'{sofc_name}_{current_density[i]}'
                    _rows = []
                    for k in range(3):
                        for phase in ['a', 'b', 'c']:
                            tmp = np.load(f'{datapath}/{res}_005Kusano{C}-{p}/{k}/{phase}/{sofc_name}.npy')
                            _rows.append(tmp)
                    data.loc[idx, 0] = current_density[i]
                    for j in range(0, META_N):
                        data.loc[idx][res ** 2 * j + 1:res ** 2 * j + res ** 2 + 1] = _rows[j]
                    if 7 == i:
                        target.loc[idx] = 0.0
                    else:
                        target.loc[idx] = file.iloc[i, 1]
            data.to_pickle(f'../data/3d_frames/v_{VERSION}/{dataset}_data_test.pkl')
            target.to_pickle(f'../data/3d_frames/v_{VERSION}/{dataset}_target_test.pkl')

# In[58]:


idx_names = []
for sofc_name in names_list[test_size + train_size:]:
    file = pd.read_csv(f'{namespath + sofc_name}_{TEMPERATURE}_3d.csv', header=None)
    for i in range(8):
        idx = f'{sofc_name}_{current_density[i]}'
        idx_names.append(idx)

# In[59]:
valid_names = names_list[test_size + train_size:]
# In[62]:

for C in c_set:
    for p in p_set:
        for res in res_set:
            datapath = f'../data/pi/{res}'
            data = pd.DataFrame(columns=np.arange(res ** 2 * META_N + 1), index=idx_names, dtype='float64')
            target = pd.Series(index=idx_names)
            dataset = f'{res}_005Kusano{C}-{p}{SET_NAME}'
            for sofc_name in valid_names:
                file = pd.read_csv(f'{namespath + sofc_name}_{TEMPERATURE}_3d.csv', header=None)
                for i in range(8):
                    idx = f'{sofc_name}_{current_density[i]}'
                    _rows = []
                    for k in range(3):
                        for phase in ['a', 'b', 'c']:  # <--- changes no 'a'
                            tmp = np.load(f'{datapath}/{res}_005Kusano{C}-{p}/{k}/{phase}/{sofc_name}.npy')
                            _rows.append(tmp)
                    data.loc[idx, 0] = current_density[i]
                    for j in range(0, META_N):
                        data.loc[idx][res ** 2 * j + 1:res ** 2 * j + res ** 2 + 1] = _rows[j]
                    if 7 == i:
                        target.loc[idx] = 0.0
                    else:
                        target.loc[idx] = file.iloc[i, 1]
            data.to_pickle(f'../data/3d_frames/v_{VERSION}/{dataset}_data_valid.pkl')
            target.to_pickle(f'../data/3d_frames/v_{VERSION}/{dataset}_target_valid.pkl')
