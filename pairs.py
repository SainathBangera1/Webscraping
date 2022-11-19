import pandas as pd
import numpy as np
from dfunctions import pairUp, compareList, pairTostring
import ast
import csv
import time

data = pd.read_csv('dataset.csv')
# data1 is just array of 6 ball numbers
data1 = np.array(data[['1st Digit', '2nd Digit', '3rd Digit',
                 '4th Digit', '5th Digit', '6th Digit']])

pair_Nums = pairUp(data1)

pair_Array = []

for j in pair_Nums:
    for k in j:
        pair_Array.append(k)

pair_Arr = []
for l in pair_Array:
    sorted = l
    sorted.sort()
    pair_Arr.append(str(sorted))

pair_Arr = list(set(pair_Arr))

# print(len(pair_Arr))

pair_Arr_New = []

for n in pair_Arr:
    pair_Arr_New.append(ast.literal_eval(n))

pairs_Frequency = []


start = time.perf_counter()
# calls the function
for o in pair_Arr_New:
    pairs_Frequency.append([pairTostring(o), compareList(data1, o)])
# record end time
end = time.perf_counter()
ms = (end-start) * 10**6
print(f"It took {ms:.03f} micro secs to get pairs_Frequency Array")

pairs_CSV_TITLE = ['Pairs', 'Frequency']

with open('pairs_CSV.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(pairs_CSV_TITLE)
    for i in pairs_Frequency:
        myFile.writerow(i)

print("Done Writing pairs_CSV.csv file . . .")
