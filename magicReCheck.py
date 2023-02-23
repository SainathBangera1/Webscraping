import pandas as pd
import numpy as np
import csv
import random
from dfunctions import matchNum

number=[]

for i in range(5):
    num = int(input(f"Enter Number {i+1} : "))
    number.append(num)

data = pd.read_csv('magic2_generated.csv')
data = np.array(data[["Digit_1","Digit_2","Digit_3","Digit_4","Digit_5"]])
srno=0
for i in data:
    count=0
    for j in i:
        for k in number:
            if(k==j):
                count+=1
    srno+=1
    print(f"For number in row {srno} : {count} numbers match")
        
    