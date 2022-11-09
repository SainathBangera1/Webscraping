import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import sys
import matplotlib
matplotlib.use('Agg')

df = pd.read_csv('deltas.csv')
# data = df[['1st Digit']]
# print(data.corr())
# df['6th_Prob'].plot(kind='hist')
# data.plot()
# plt.show()

# Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

df.plot(kind='scatter', x='Ball Number', y='Point 1')

plt.show()
