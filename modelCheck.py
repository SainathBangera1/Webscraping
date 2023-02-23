import pandas as pd
import numpy as np
import csv
import random
from dfunctions import matchNum

number=[]

for i in range(20):
    num = int(input(f"Enter Number {i+1} : "))
    number.append(num)

data = pd.read_csv('modelONE.csv')
data = np.array(data[["Digit1","Digit2","Digit3","Digit4","Digit5","Digit6","Digit7","Digit8","Digit9","Digit10"]])
srno=0
for i in data:
    count=0
    for j in i:
        for k in number:
            if(k==j):
                count+=1
    srno+=1
    print(f"For number in row {srno} : {count} numbers match")
        
    