import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error, mean_absolute_error, \
    mean_absolute_percentage_error

df = pd.read_pickle('../data/results/representative_predictions_50.pkl')
scores = dict()
scores['r2'] = r2_score(df['true'], df['pred'])
scores['mse'] = mean_squared_error(df['true'], df['pred'])
scores['rmse'] = root_mean_squared_error(df['true'], df['pred'])
scores['mae'] = mean_absolute_error(df['true'], df['pred'])
scores['mape'] = mean_absolute_percentage_error(df['true'], df['pred'])
scores['corr'] = df[['true', 'pred']].corr(method='pearson').iloc[0, 1]

mse = (df['true'] - df['pred'])**2
print(mse.describe())
print(mse[mse > 1e-4].shape[0] / len(mse))

for k, v in scores.items():
    print(f'{k}: {v}')

