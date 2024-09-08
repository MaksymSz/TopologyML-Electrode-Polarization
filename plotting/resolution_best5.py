import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter

import mpl_config  # matplotlib configs

PLOT_COLOR = '#a781c7'

data = pd.read_pickle('../data/results/resolution_bo5.pkl')
data['trend'] = data.iloc[:, 2]

x = [int(x.split('_')[0]) for x in data.index]

fig, ax = plt.subplots(figsize=(2.9, 2.9))
ax.plot(x, data.trend, linestyle='solid', marker='.', color=PLOT_COLOR, label='median')
ax.fill_between(x, data.min(axis=1), data.max(axis=1), alpha=0.2, color=PLOT_COLOR, label='minimum/maximum')
plt.yticks([])
plt.yscale('log')
plt.gca().tick_params(axis='both', direction='in', which='both', left=True, right=False)
plt.gca().tick_params(axis='y', which='both', length=0)
plt.xlabel(r'Persistence Image resolution', fontsize=8)
plt.ylabel(r'Overpotential $\hat{\eta}$ MSE $/\; \mathrm{V}^2$', fontsize=10)
plt.grid(False)

ax = plt.gca()

ddd = {0, 1e-4, 1e-3, 1e-2}


def custom_formatter_xaxis(x, pos):
    if x == -1:
        return ''
    return f'{int(x)}'


def custom_formatter_yaxis(x, pos):
    if x in ddd:
        s = f'{x:1E}'[-1:]
        return '$10^{-' + s + '}$'
    return ''


ax.xaxis.set_major_locator(ticker.FixedLocator(ax.get_xticks()))
ax.xaxis.set_major_formatter(FuncFormatter(custom_formatter_xaxis))

ax.yaxis.set_major_locator(ticker.FixedLocator(ax.get_yticks()))
ax.yaxis.set_major_formatter(FuncFormatter(custom_formatter_yaxis))
plt.xlim(left=0)

plt.tight_layout()
plt.tick_params(axis='y', which='major', length=3.5)
plt.legend()
plt.savefig('plots/pi_resolution_bo5.pdf', transparent=False, dpi=600)
plt.show()
