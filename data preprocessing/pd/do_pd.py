from multiprocessing import Pool
import os
from make_filtration import generate_pds
from time import perf_counter
from pathlib import Path

data_path = Path('../../data')

os.chdir(data_path / 'raw')

sofc = []

for item in os.listdir():
    if os.path.isfile(item):
        sofc.append(item.replace('.zip', ''))

if __name__ == '__main__':
    t0 = perf_counter()

    IMGS = len(sofc)
    print('sofcs: ', IMGS)

    with Pool() as pool:
        # define range of each task
        _proc_num = pool._processes
        _start = IMGS // _proc_num
        _rest = IMGS % _proc_num
        tasks = [(i * _start, (i + 1) * _start) for i in range(_proc_num)]

        if _rest:
            tasks[-1] = ((_proc_num - 1) * _start, _proc_num * _start + _rest)

        r = []
        for i in range(_proc_num):
            r.append(pool.apply_async(generate_pds, args=(tasks[i],)))

        t1 = perf_counter()
        print(f'Initialization took {t1 - t0} seconds')

        # start tasks
        t0 = perf_counter()
        f_r = [_.get() for _ in r]
        t1 = perf_counter()
        print(f'Computation took {t1 - t0} seconds')
