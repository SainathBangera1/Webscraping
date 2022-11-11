import matplotlib.pyplot as plt
import ast
import numpy as np
import pandas as pd
import csv
import sys
import matplotlib
from dfunctions import date_format
# matplotlib.use('Agg')


############################## TIME DELTAS ##################################
df_delta = pd.read_csv('deltas.csv')

df_delta["Mean"] = df_delta.iloc[:, 1:].mean(axis=1, skipna=True)
df_delta = df_delta.replace('NaN', np.nan)
df_delta = df_delta.fillna(0)
df_delta["Max_Mean"] = df_delta.iloc[:, 1:].mean(axis=1, skipna=True)
# df_transpose = df.T

# for d in dataNew:
#     print(f"{int(d[0])}, {d[1]}")


data = pd.read_csv('dataset.csv')
data = np.array(data[['List_Date', '1st Digit', '2nd Digit',
                '3rd Digit', '4th Digit', '5th Digit', '6th Digit']])

# to get first appearance date for all Numbers

first_Date_Apperance = []

for i in range(1, 91):
    for x in data:
        if i in [x[1], x[2], x[3], x[4], x[5], x[6]]:
            first_Date_Apperance.append(date_format(ast.literal_eval(x[0])))
            break

df_delta["First_Date"] = first_Date_Apperance

dataNew = np.array(df_delta[["Ball Number", "First_Date", "Mean"]])

# Round of the Time Delats Mean to whole number
for d in dataNew:
    d[2] = round(d[2])

print("dataNew loaded from pdClassifier.py..")
# for d1 in dataNew:
#     print(d1)
# to save dataframe in CSV file
# df.to_csv('deltas.csv', index=False)
# print("Done writing deltas.csv file..")
# data = df[['1st Digit']]
# print(data.corr())
# df['6th_Prob'].plot(kind='hist')

# data.plot()
# plt.show()

# Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

# df.plot(kind='scatter', x='Ball Number', y='Mean')

# plt.show()
