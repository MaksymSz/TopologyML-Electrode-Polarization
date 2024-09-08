import imageio
import numpy as np
import homcloud.interface as hc
import os
from zipfile import ZipFile
from pathlib import Path

PHASES = [0, 127, 255]
PHASE_NAME = {0: 'a', 127: 'b', 255: 'c'}
DATA_PATH = Path("../../data")

# get resolution
os.chdir(DATA_PATH / 'raw')
sofc = []
for item in os.listdir():
    if os.path.isfile(item):
        sofc.append(item.replace('.zip', ''))


def generate_pds(args):
    start, end = args

    for item in sofc[start:end]:
        with ZipFile(item + '.zip', 'r') as archive:
            pict = np.stack([
                imageio.v3.imread(archive.read(f'{item}/slices_bmp/Micro{n:04d}.bmp'))
                for n in range(200)
            ], axis=0)
            for phase in PHASES:
                pdlist = hc.PDList.from_bitmap_levelset(hc.distance_transform(pict == phase, signed=True))
                for i in range(3):
                    pd = pdlist.dth_diagram(i)
                    stacked = np.column_stack(pd.birth_death_times())
                    unique = np.column_stack(np.unique(stacked, axis=0, return_counts=True))
                    np.save(
                        DATA_PATH / f'pds/{i}/{PHASE_NAME[phase]}/{item + ".npy"}',
                        unique)
