import pandas as pd
import numpy as np
import csv
import random
from dfunctions import matchNum

number=[]

for i in range(20):
    num = int(input(f"Enter Number {i+1} : "))
    number.append(num)


print("Following are the model names of csv file available")
print("1. 5pmKENORANGE.csv")

time=input("Enter any one model name from the the above : ")

csvURL = time+'.csv'
data = pd.read_csv(csvURL)
data = np.array(data[["Digit1","Digit2","Digit3","Digit4","Digit5","Digit6","Digit7","Digit8","Digit9","Digit10"]])
srno=0

cost=[]

for i in data:
    count=0
    for j in i:
        for k in number:
            if(k==j):
                count+=1
    if(count==4 or count==5 or count==6 or count==7 or count==8):
        cost.append(count)

    srno+=1
    print(f"For number in row {srno} : {count} numbers match")
        
total_amt=0

for i in cost:
    if(i==4):
        total_amt+=20
    elif(i==5):
        total_amt+=40
    elif(i==6):
        total_amt+=200
    elif(i==7):
        total_amt+=1000
    elif(i==8):
        total_amt+=9000

invest = int(input("Enter the number of tickets bought: "))

print(f"Total amount invested  = {20*invest} Rs")
print(f"Total amount generated  = {total_amt} Rs")
print(f"Net Profit = {total_amt - 20*invest} Rs")