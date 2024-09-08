import matplotlib.pyplot as plt
import pandas as pd

import mpl_config  # matplotlib configs

curves = pd.read_pickle('../data/results/representative_predictions_50.pkl')
plt.figure(figsize=(2.9, 2.9))
plt.scatter(curves.true, curves.pred, s=10, c='#64b5f6', alpha=0.3)
plt.plot([-1, 1], [-1, 1], label='Diagonal Line', linestyle='--', color='black', linewidth=1)

axs = plt.gca()

axs.label_outer()
axs.tick_params(axis='both', direction='in', which='both')
delta_max = 0.05
delta_min = 1.5
plt.xlim([-0.005246 * (1 + delta_min), 0.197136 * (1 + delta_max)])
plt.ylim([-0.005246 * (1 + delta_min), 0.197136 * (1 + delta_max)])
plt.gca().set_aspect('equal', adjustable='box')

ticks = [0, 0.05, 0.1, 0.15, 0.2]
plt.xticks(ticks)
plt.yticks(ticks)

plt.xlabel(r'RMSE:', fontsize=9)
plt.ylabel(r'RMSE:', fontsize=9)
plt.subplots_adjust(left=0.2, right=0.97, top=1, bottom=0.09)

ticks = axs.yaxis.get_major_ticks()
ticks[-1].tick1line.set_visible(False)
ticks[-2].tick1line.set_visible(False)
ticks[-3].tick1line.set_visible(False)

plt.savefig('plots/scatter.pdf', transparent=True)

plt.show()
