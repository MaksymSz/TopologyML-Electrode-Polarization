from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter

import mpl_config  # matplotlib configs

colors = ['#000075', '#f032e6', '#e6194B']
targetpath = Path('../data/pi')

plt.figure(figsize=(2.9, 2.9))
bins = [27, 11, 5]


def get_data(x):
    true = pd.read_pickle(targetpath / f'50_005Kusano3-1__{x}_target_test.pkl')
    with open(f'final_data/hist_pred_{x}.pkl', 'rb') as handler:
        pred = pickle.load(handler)
    data = pd.DataFrame(true)
    data[1] = pred
    data['mse'] = (data[0] - data[1]) ** 2
    return data


for idx, s in enumerate([100, 200, 400]):
    data = get_data(s)
    label = f'SOFC in test set: {s}'
    mse = data.mse
    plt.hist(mse, log=True, histtype='step', fill=False,
             alpha=1,
             bins=bins[idx],
             color=colors[idx],
             linewidth=1.3,
             label=f'{label}',
             )

plt.gca().tick_params(axis='both', direction='in', which='both', left=True, right=False)
plt.gca().tick_params(axis='y', which='both', length=0)
plt.xlabel(r'Overpotential $\hat{\eta}$ MSE $/\; \mathrm{V}^2$', fontsize=10)
plt.ylabel('Occurrence', fontsize=10)

ddd = {0, 0.1, 1, 10, 100, 1000, 10_000}


def custom_formatter_yaxis(x, pos):
    if x in ddd:
        s = f'{x:1E}'[-1:]
        return '$10^{' + s + '}$'
    return ''


ax = plt.gca()
ax.yaxis.set_major_locator(ticker.FixedLocator(ax.get_yticks()))
ax.yaxis.set_major_formatter(FuncFormatter(custom_formatter_yaxis))
plt.tick_params(axis='y', which='major', length=3.5)

plt.xlim(left=0)

plt.legend()

plt.tight_layout()

plt.savefig('plots/histograms.pdf', transparent=True)
plt.show()
