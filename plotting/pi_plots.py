import pandas as pd
import matplotlib.pyplot as plt

import mpl_config  # matplotlib configs

COLOR = 'black'

Cset = [1, 10, 20, 50, 100, 200, 500]
pset = [1, 10, 20, 50, 100, 200, 500]

fig, axs = plt.subplots(nrows=7, ncols=7, sharex=True, sharey=True, figsize=(2.9, 2.9))

df = pd.read_pickle('../data/pi/pi_plots.pkl')

for Cid, C in enumerate(Cset[::-1]):
    for pid, p in enumerate(pset):
        __i = 3
        im = df.loc[f'{C}-{p}'].to_numpy().reshape(15, 15)
        axs[Cid, pid].imshow(im[::-1], cmap='plasma')
        axs[Cid, pid].axis('off')

        if pid == 0:
            axs[Cid, pid].text(-6, 7, C, fontsize=plt.rcParams['font.size'], rotation=0,
                               verticalalignment='center',
                               color=COLOR)
        if C == 1:
            axs[Cid, pid].text(7, 18, p, fontsize=plt.rcParams['font.size'], rotation=0,
                               verticalalignment='center',
                               horizontalalignment='center',
                               color=COLOR)

plt.axis('off')
plt.text(-92, -40, 'C', fontsize=plt.rcParams['font.size'], rotation=90,
         verticalalignment='center',
         horizontalalignment='center',
         color=COLOR)
plt.text(-34, 22, 'p', fontsize=plt.rcParams['font.size'], rotation=0,
         verticalalignment='center',
         horizontalalignment='center',
         color=COLOR)

plt.subplots_adjust(left=0.1, right=0.95, top=1, bottom=0.1, wspace=0.07, hspace=0.05)
plt.savefig('plots/pi_plots.pdf')
plt.show()
