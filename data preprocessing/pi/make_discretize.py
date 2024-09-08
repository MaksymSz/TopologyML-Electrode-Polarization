from computing.transformations import transform_pairs
from computing.core import discretize
import numpy as np
import os
from pathlib import Path

PHASES = [0, 127, 255]
PHASE_NAME = {0: 'a', 127: 'b', 255: 'c'}
""" used shortcuts for SOFC phases
a - pores
b - YSZ
c - nickel
"""
DATA_PATH = Path('../../data')

os.chdir(DATA_PATH / '3d_neumann')

sofc = []
for item in os.listdir():
    if os.path.isfile(item):
        sofc.append(item[:-11])

os.chdir(DATA_PATH)


def generate_pi(args):
    start, end, resolution = args
    print(args)

    _init_data = transform_pairs(np.load('..data/init_array.npy'))
    _ = discretize(_init_data, 1)

    for item in sofc[start:end]:
        for betti in range(3):
            for phase in PHASES:
                pairs = np.load(
                    DATA_PATH / f'pds/{betti}/{PHASE_NAME[phase]}/{item}.npy')
                transformed_pairs = transform_pairs(pairs)
                pi = discretize(transformed_pairs, resolution)
                np.save(
                    f'D:/new_15_pi/{resolution}/{str(resolution)}_005Kusano500-50/{betti}/{PHASE_NAME[phase]}/{item}.npy',
                    pi)
