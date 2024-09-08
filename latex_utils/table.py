import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import pprint

curves = pd.read_pickle('../data/results/representative_curves_50.pkl')

df = pd.DataFrame(index=curves.index)
for i in np.arange(0, 4, 0.5):
    df[i] = (curves[f'true_{i}'] - curves[f'pred_{i}']) / (curves[f'true_{i}'] if i != 0 else 1)

df['rmse'] = curves.rmse
stats = df.describe()
stats.loc['95%', :] = df.quantile(0.95)
stats = stats.reindex(['count', 'mean', 'std', 'min', '25%', '50%', '75%', '95%', 'max'])

for i in np.arange(0, 4, 0.5):
    stats.loc['PCC', i] = curves[[f'true_{i}', f'pred_{i}']].corr(method='pearson').iloc[0, 1]
    stats.loc['SCC', i] = curves[[f'true_{i}', f'pred_{i}']].corr(method='spearman').iloc[0, 1]

### NEEDED INFO
predictions = pd.read_pickle('../data/results/representative_predictions_50.pkl')
predictions['mse'] = (predictions.true - predictions.pred) ** 2
predictions['rmse'] = ((predictions.true - predictions.pred) ** 2) ** 0.5

rep_model_info = dict()

rep_model_info['R2 score'] = r2_score(predictions.true, predictions.pred)
rep_model_info['MAE'] = mean_absolute_error(predictions.true, predictions.pred)
rep_model_info['MSE'] = mean_squared_error(predictions.true, predictions.pred)
rep_model_info['RMSE'] = root_mean_squared_error(predictions.true, predictions.pred)

rep_model_info['range min'] = predictions.mse.min()
rep_model_info['range max'] = predictions.mse.max()

rep_model_info['greater than 0.01'] = (df.rmse > 0.01).sum()  # curves
rep_model_info['close to 0'] = (abs(df[0.0]) < 1e-4).sum()  # curves
rep_model_info['less than 0'] = (df[0.0] < 0).sum()  # curves

rep_model_info['75%'] = predictions.mse.quantile(0.75)
rep_model_info['95%'] = predictions.mse.quantile(0.95)
rep_model_info['std'] = predictions.mse.std()
rep_model_info['mean'] = predictions.mse.mean()

pprint.pp(rep_model_info)

predictions.mse.hist(bins=100)
plt.axvline(predictions.mse.quantile(0.95), label='95%', color='r')
plt.axvline(predictions.mse.quantile(0.75), label='75%', color='g')
plt.axvline(predictions.mse.min(), color='k')
plt.axvline(predictions.mse.max(), color='k')

with open('../plotting/plots/table.tex', 'w') as table:
    table.write("""\\begin{tabular}{|crrrrrrrr|}
\hline
\\rowcolor[HTML]{9B9B9B} 
{\color[HTML]{000000} J} &
  \multicolumn{1}{c}{\cellcolor[HTML]{9B9B9B}{\color[HTML]{000000} 0.0}} &
  \multicolumn{1}{c}{\cellcolor[HTML]{9B9B9B}0.5} &
  \multicolumn{1}{c}{\cellcolor[HTML]{9B9B9B}1.0} &
  \multicolumn{1}{c}{\cellcolor[HTML]{9B9B9B}1.5} &
  \multicolumn{1}{c}{\cellcolor[HTML]{9B9B9B}2.0} &
  \multicolumn{1}{c}{\cellcolor[HTML]{9B9B9B}2.5} &
  \multicolumn{1}{c}{\cellcolor[HTML]{9B9B9B}3.0} &
  \multicolumn{1}{c|}{\cellcolor[HTML]{9B9B9B}3.5} \\\\ \hline
\\rowcolor[HTML]{FFFFFF} """)
    for i in range(1, stats.shape[0]):
        color = 'FFFFFF' if i % 2 == 1 else 'EFEFEF'
        res = "\\rowcolor[HTML]{" + color + "} \n"
        res += stats.index[i] + ' & '
        for j in range(stats.shape[1] - 1):
            res += str(round(stats.iloc[i, j], 6)) + " & "
        else:
            res = res[:-2] + ' \\\\'

        res = res.replace('%', 'th')
        res = res.replace('mean', r'$\mu$')
        res = res.replace('std', r'$\sigma$')
        res = res.replace('nan', r'\multicolumn{1}{c}{\cellcolor[HTML]{' + color + r'}\textbf{--}}')
        table.write(res + '\n')

    table.write("""\hline
\end{tabular}%
\end{table*}""")
