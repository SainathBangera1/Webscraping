import pandas as pd
import numpy as np
from dfunctions import pairUp, compareList, pairTostring, strToarray, checkPairInArr, lisToDate
import ast
import csv
import time

data = pd.read_csv('dataset.csv')
data_1 = np.array(data[["List_Date", "1st Digit", "2nd Digit",
                  "3rd Digit", "4th Digit", "5th Digit", "6th Digit"]])

data_1_Latest = []

for i in range(len(data_1)-1, -1, -1):
    data_1_Latest.append(data_1[i])


pairs_Data = pd.read_csv('pairs_CSV.csv')
pairs_Data_1 = np.array(pairs_Data[["Pairs", "Frequency"]])

pairs_Data_1_NEW = []
pairs_Data_2_NEW = []

for i in pairs_Data_1:
    pairs_Data_1_NEW.append([strToarray(i[0]), i[1]])

start = time.perf_counter()
# calls the function
for j in pairs_Data_1_NEW:
    dates_str = checkPairInArr(j[0], data_1_Latest)
    pairs_Data_2_NEW.append([pairTostring(j[0]), j[1], dates_str])
# record end time
end = time.perf_counter()
ms = (end-start) * 10**6

print(f"It took {ms:.03f} micro secs to get pairs_Frequency_Dates Array")

pairs_Freq_CSV_TITLE = ['Pairs', 'Frequency', 'Dates']

with open('pairs_Freq_CSV.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(pairs_Freq_CSV_TITLE)
    for i in pairs_Data_2_NEW:
        myFile.writerow(i)

print("Done Writing pairs_Freq_CSV.csv file . . .")
