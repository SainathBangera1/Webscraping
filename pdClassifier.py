import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import sys
import matplotlib
matplotlib.use('Agg')

df = pd.read_csv('deltas.csv')

df["Mean"] = df.iloc[:, 1:].mean(axis=1, skipna=True)
df = df.replace('NaN', np.nan)
df = df.fillna(0)
df["Max_Mean"] = df.iloc[:, 1:].mean(axis=1, skipna=True)
# df_transpose = df.T
data = df['Mean']
print(df.head())

# to save dataframe in CSV file
df.to_csv('deltas.csv', index=False)
print("Done writing deltas.csv file..")
# data = df[['1st Digit']]
# print(data.corr())
# df['6th_Prob'].plot(kind='hist')

data.plot()
plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

# df.plot(kind='scatter', x='Ball Number', y='Mean')

# plt.show()
