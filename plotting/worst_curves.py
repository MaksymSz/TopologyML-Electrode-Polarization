from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from matplotlib.lines import Line2D
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter

import mpl_config

PI_RESOLUTION = 50
datapath = Path(f'../data/pi/50_005Kusano3-1__400_data_test.pkl')
targetpath = Path(f'../data/pi/50_005Kusano3-1__400_target_test.pkl')
neumann_path = Path(f'../data/3d_neumann/')
modelpath = f'../models/representative_model.keras'


def prepare_inputs(pi_resolution):
    model_inputs = {'current': slice(0, 1)}
    i = 0
    for k in range(3):
        for p in ['a', 'b', 'c']:
            model_inputs[f'b{k}_p{p}'] = slice(i * pi_resolution ** 2 + 1, (i + 1) * pi_resolution ** 2 + 1)
            i += 1
    return model_inputs


data = pd.read_pickle(datapath)
target = pd.read_pickle(targetpath)
X_test, y_test = data, target

inputs_slices = prepare_inputs(PI_RESOLUTION)
model = tf.keras.models.load_model(modelpath)

curves = pd.read_pickle('../data/results/representative_curves_50.pkl')
curves = curves.sort_values(by='rmse', ascending=False)

sofc_ids = [0, 4, 8]
K = len(sofc_ids)

colors = ['#e57373', '#ba68c8', '#7986cb']

scale = 0.80
fig, axs = plt.subplots(figsize=(6.3 * scale, 4 * scale))


def get_curve(sofc_id, k):
    worst_index = curves.index[sofc_id]
    print(worst_index)
    worst_x = data.loc[worst_index + '_1.0']
    current = np.arange(0.0, 3.6, 0.1)
    print(len(current))
    worst_x = np.repeat(worst_x.to_numpy().reshape(1, -1), current.shape[0], axis=0)
    worst_x[:, 0] = current
    worst_x = [
        worst_x[:, inputs_slices['current']],
        worst_x[:, inputs_slices['b0_pa']],
        worst_x[:, inputs_slices['b0_pb']],
        worst_x[:, inputs_slices['b0_pc']],
        worst_x[:, inputs_slices['b1_pa']],
        worst_x[:, inputs_slices['b1_pb']],
        worst_x[:, inputs_slices['b1_pc']],
        worst_x[:, inputs_slices['b2_pa']],
        worst_x[:, inputs_slices['b2_pb']],
        worst_x[:, inputs_slices['b2_pc']],
    ]

    worst_y = model.predict(worst_x)
    worst_true = pd.read_csv(
        neumann_path / f'{worst_index}_800_3d.csv',
        header=None)
    print('\t\t', min(worst_y), max(worst_y))
    label = f'RMSE = {curves.loc[worst_index, "rmse"]:.4e}'
    axs.plot(current * 1000, worst_y, color=colors[k], marker='None', linestyle='solid', label=label)
    axs.plot(worst_true.iloc[:, 0], worst_true.iloc[:, 1], color=colors[k], marker='o', linestyle='None')
    axs.set_xlabel(r'Current $J \; /\;(\mathrm{A} / \mathrm{m}^2)$', fontsize=10)
    axs.set_ylabel(r'Overpotential $\eta\; / \;\mathrm{V}$', fontsize=10)  # \quad
    axs.set_xticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500])
    axs.set_xlim(left=0, right=3550)
    axs.set_ylim(bottom=-0.0068, top=0.21)
    axs.grid(False)


# Generate all curves
for k in range(K):
    get_curve(sofc_ids[k], k)

axs.label_outer()
axs.tick_params(axis='both', direction='in', which='both')

custom_handles = []
custom_labels = []

colors_c = ['k']
markers_c = ['o', 'None']
handles = [
              Line2D([0], [0], color=color, linestyle='solid', lw=2) for color in colors_c
          ] + [
              Line2D([0], [0], color='w', markerfacecolor=color, marker=marker, markersize=10) for color, marker in
              zip(colors_c, markers_c)
          ]
custom_handles.extend(handles)
custom_labels.extend(['Representative model', 'Numerical model'])

custom_handles.extend([Line2D([0], [0], color=color, marker='s', markersize=8, linestyle='None') for color in colors])
results = [f'{curves.iloc[sofc_ids[k]]["rmse"]:.4e}' for k in range(K)]
results = [x.split('-') for x in results]
results = [f"${x[0][:-1]} \\times 10^" + "{-" + f"{x[1][1]}" + "}$" for x in results]
custom_labels.extend(results)


def custom_formatter(x, pos):
    return f'{int(x)}'


axs.xaxis.set_major_locator(ticker.FixedLocator(axs.get_xticks()))
axs.xaxis.set_major_formatter(FuncFormatter(custom_formatter))

fig.legend(custom_handles, custom_labels, frameon=False, loc='center', bbox_to_anchor=(0.32, 0.76), fontsize=9)

plt.tight_layout()
plt.savefig('plots/rmse_test.pdf', dpi=600)
plt.show()
