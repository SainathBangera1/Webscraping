import pandas as pd
import numpy as np
import csv
import random
from dfunctions import matchNum

number=[]

for i in range(6):
    num = int(input(f"Enter Number {i+1} : "))
    number.append(num)

csvURL = 'superTICKETS.csv'
data = pd.read_csv(csvURL)
data = np.array(data[["Digit1","Digit2","Digit3","Digit4","Digit5","Digit6"]])
srno=0

cost=[]

for i in data:
    count=0
    for j in i:
        for k in number:
            if(k==j):
                count+=1
    if(count==2 or count==3 or count==4 or count==5):
        cost.append(count)

    srno+=1
    print(f"For number in row {srno} : {count} numbers match")
        
total_amt=0

for i in cost:
    if(i==2):
        total_amt+=5.63
    elif(i==3):
        total_amt+=29.26
    elif(i==4):
        total_amt+=422.49
    elif(i==5):
        total_amt+=59503.17

total_amt=total_amt*80
invest = int(input("Enter the number of tickets bought: "))

print(f"Total amount invested  = {168*invest} Rs")
print(f"Total amount generated  = {total_amt} Rs")
print(f"Net Profit = {total_amt - 168*invest} Rs")