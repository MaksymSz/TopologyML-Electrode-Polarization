import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

import mpl_config  # matplotlib configs

df = pd.read_pickle('../data/results/heatmap.pkl')
df = df.astype('float')

scale = 1.2
figsize = (2.9, 2.9)
fig, ax = plt.subplots(figsize=figsize)

formatter = tkr.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-2, 2))

annots = np.empty(shape=(df.shape[0], df.shape[1]), dtype=object)
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        annot = f'{df.iloc[i, j]:.2e}'
        if i == 0 and j == 0:
            annot = str(float(annot.split('e')[0]) / 10)
        annots[i, j] = annot[:4]
ax = sns.heatmap(df, annot=annots, fmt='', square=True, cmap=sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True),
                 ax=ax,
                 cbar_kws={'shrink': 0.64, "format": formatter})

ax.invert_yaxis()
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

plt.xlabel("p")
plt.ylabel("C")

plt.subplots_adjust(left=0.16, right=1, top=1.1, bottom=-0.07
                    , wspace=0.1, hspace=0.1)

plt.savefig('plots/heatmap.pdf')
plt.show()
