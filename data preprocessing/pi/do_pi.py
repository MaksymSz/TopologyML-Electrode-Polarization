import os
from time import perf_counter
from multiprocessing import Pool
from make_discretize import generate_pi
import sys

try:
    RESOLUTION = int(sys.argv[1])
except Exception as e:
    print('Error: no PI resolution specified')
    sys.exit(-1)

data_path = "../../data"
os.chdir(data_path + '/3d_neumann_v3')
sofc = []
for item in os.listdir():
    if os.path.isfile(item):
        sofc.append(item[:-11])

if __name__ == '__main__':
    d = f'{RESOLUTION}\\{RESOLUTION}_005Kusano500-50'
    if not os.path.exists(f'D:\\new_15_pi\\{RESOLUTION}'):
        os.mkdir(f'D:\\new_15_pi\\{RESOLUTION}')
    os.mkdir(f'D:\\new_15_pi\\{d}')
    os.mkdir(f'D:/new_15_pi/{d}/0')
    os.mkdir(f'D:\\new_15_pi\\{d}\\0\\a')
    os.mkdir(f'D:\\new_15_pi\\{d}\\0\\b')
    os.mkdir(f'D:\\new_15_pi\\{d}\\0\\c')
    os.mkdir(f'D:\\new_15_pi\\{d}\\1')
    os.mkdir(f'D:\\new_15_pi\\{d}\\1\\a')
    os.mkdir(f'D:\\new_15_pi\\{d}\\1\\b')
    os.mkdir(f'D:\\new_15_pi\\{d}\\1\\c')
    os.mkdir(f'D:\\new_15_pi\\{d}\\2')
    os.mkdir(f'D:\\new_15_pi\\{d}\\2\\a')
    os.mkdir(f'D:\\new_15_pi\\{d}\\2\\b')
    os.mkdir(f'D:\\new_15_pi\\{d}\\2\\c')
    t0 = perf_counter()
    _imgs = len(sofc)
    print(f'sofcs: {_imgs}')

    with Pool() as pool:
        _proc_num = pool._processes
        _start = _imgs // _proc_num
        _rest = _imgs % _proc_num
        tasks = [(i * _start, (i + 1) * _start, RESOLUTION) for i in range(_proc_num)]

        if _rest:
            tasks[-1] = ((_proc_num - 1) * _start, _proc_num * _start + _rest, RESOLUTION)

        r = []
        for i in range(_proc_num):
            r.append(pool.apply_async(generate_pi, args=(tasks[i],)))

        f_r = [_.get() for _ in r]

        print(f'Computation complete')
