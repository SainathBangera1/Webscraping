import pandas as pd
import numpy as np
import csv
import random
from dfunctions import matchNum

number=[]

for i in range(20):
    num = int(input(f"Enter Number {i+1} : "))
    number.append(num)

data = pd.read_csv('generated.csv')
data = np.array(data[["Digit_1","Digit_2","Digit_3","Digit_4","Digit_5","Digit_6","Digit_7","Digit_8","Digit_9","Digit_10"]])
srno=0
for i in data:
    count=0
    for j in i:
        for k in number:
            if(k==j):
                count+=1
    srno+=1
    print(f"For number in row {srno} : {count} numbers match")
        
    