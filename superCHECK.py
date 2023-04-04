import pandas as pd
import numpy as np
import csv
import random
from dfunctions import matchNum,date_to_Timestamp,giveSEED

number=[]

for i in range(6):
    num = int(input(f"Enter Number {i+1} : "))
    number.append(num)

csvURL = 'superTICK.csv'
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

####################################### USING TIMESTAMPS #################

# data_of_timestamp = pd.read_csv('superUNIQUETime.csv')
# data_of_timestamp1  = np.array(data_of_timestamp['DATA_1'])
# data_of_timestamp1 = data_of_timestamp1.tolist()

# data_of_timestamp2  = np.array(data_of_timestamp['DATA_2'])
# data_of_timestamp2 = data_of_timestamp2.tolist()

# data_of_timestamp3  = np.array(data_of_timestamp['DATA_3'])
# data_of_timestamp3 = data_of_timestamp3.tolist()

# data_of_timestamp4  = np.array(data_of_timestamp['DATA_4'])
# data_of_timestamp4 = data_of_timestamp4.tolist()

# data_of_timestamp5  = np.array(data_of_timestamp['DATA_5'])
# data_of_timestamp5 = data_of_timestamp5.tolist()

# data_of_timestamp6  = np.array(data_of_timestamp['DATA_6'])
# data_of_timestamp6 = data_of_timestamp6.tolist()

# data_of_timestamp7  = np.array(data_of_timestamp['DATA_7'])
# data_of_timestamp7 = data_of_timestamp7.tolist()

# data_of_timestamp8  = np.array(data_of_timestamp['DATA_8'])
# data_of_timestamp8 = data_of_timestamp8.tolist()

# number=[]

# for i in range(8):
#     num = int(input(f"Enter Number {i+1} : "))
#     number.append(num)

# day = input("Enter the day: ")
# month = input("Enter the month: ")
# year = input("Enter the year: ")

# dateTimeStr = day+'/'+month+'/'+year+' '+'20:00:00'

# timestamp = int(date_to_Timestamp(dateTimeStr))
# seeds=[]
# seeds.insert(0,giveSEED(timestamp,data_of_timestamp1,number,0))
# seeds.insert(1,giveSEED(timestamp,data_of_timestamp2,number,1))
# seeds.insert(2,giveSEED(timestamp,data_of_timestamp3,number,2))
# seeds.insert(3,giveSEED(timestamp,data_of_timestamp4,number,3))
# seeds.insert(4,giveSEED(timestamp,data_of_timestamp5,number,4))
# seeds.insert(5,giveSEED(timestamp,data_of_timestamp6,number,5))
# seeds.insert(6,giveSEED(timestamp,data_of_timestamp7,number,6))
# seeds.insert(7,giveSEED(timestamp,data_of_timestamp8,number,7))

# print(f"Date : {day}/{month}/{year}")
# print(f"Numbers of the day = {number}")
# print(f"Following are the seeds = {seeds}")
# print(f"DELTA SEEDS = {seeds[0]-timestamp} , {seeds[1]-timestamp}, {seeds[2]-timestamp}, {seeds[3]-timestamp} , {seeds[4]-timestamp} , {seeds[5]-timestamp} , {seeds[6]-timestamp} , {seeds[7]-timestamp}")

# numbersMatch=[]

# for i in range(len(seeds)):
#     np.random.seed(seeds[i])
#     if(i==0):
#         num=np.random.randint(1,66)
#         numbersMatch.append(num)
#     if(i==1):
#         num=np.random.randint(2,83)
#         numbersMatch.append(num)
#     if(i==2):
#         num=np.random.randint(4,86)
#         numbersMatch.append(num)
#     if(i==3):
#         num=np.random.randint(9,88)
#         numbersMatch.append(num)
#     if(i==4):
#         num=np.random.randint(14,90)
#         numbersMatch.append(num)
#     if(i==5):
#         num=np.random.randint(26,91)
#         numbersMatch.append(num)
#     if(i==6):
#         num=np.random.randint(1,91)
#         numbersMatch.append(num)
#     if(i==7):
#         num=np.random.randint(1,91)
#         numbersMatch.append(num)

# print(f"Numbers Generated from UNIQUE DATAPOINTS : {numbersMatch}")