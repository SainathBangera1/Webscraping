import pandas as pd
import numpy as np
import csv
import json
from dfunctions import spitZero

# Opening JSON file
file = open('periodicTable.json')
  
# returns JSON object as 
# a dictionary
data_JSON = json.load(file)

data = pd.read_csv('8PM_FirstSET.csv')
data = np.array(data['Digit1'])
data = spitZero(data)

arr1 = []
tmp=data
count=0
while (count!=537):
    arr1=[]
    for i in range(len(tmp)):
        if(i+1 <len(tmp)):
            diff = tmp[i+1] - tmp[i]
            arr1.append(abs(diff)) #at 530 count of AP the numbers overflow hence using absolute values only
    tmp=arr1
    count+=1

for i in arr1:
    print(i)

print(f"original data size: {len(data)}")
print(f"after AP the size : {len(arr1)}")