import pandas as pd
import numpy as np
import csv
import random
from dfunctions import date_to_Timestamp,getNumfromSEED,generateNum,date_to_Timestamp,genNUMtimestamp

data_of_timestamp = pd.read_csv('superUNIQUETime.csv')
data_of_timestamp1  = np.array(data_of_timestamp['DATA_1'])
data_of_timestamp1 = list(set(data_of_timestamp1.tolist()))

data_of_timestamp2  = np.array(data_of_timestamp['DATA_2'])
data_of_timestamp2 = list(set(data_of_timestamp2.tolist()))

data_of_timestamp3  = np.array(data_of_timestamp['DATA_3'])
data_of_timestamp3 = list(set(data_of_timestamp3.tolist()))

data_of_timestamp4  = np.array(data_of_timestamp['DATA_4'])
data_of_timestamp4 = list(set(data_of_timestamp4.tolist()))

data_of_timestamp5  = np.array(data_of_timestamp['DATA_5'])
data_of_timestamp5 = list(set(data_of_timestamp5.tolist()))

data_of_timestamp6  = np.array(data_of_timestamp['DATA_6'])
data_of_timestamp6 = list(set(data_of_timestamp6.tolist()))

data_of_timestamp7  = np.array(data_of_timestamp['DATA_7'])
data_of_timestamp7 = list(set(data_of_timestamp7.tolist()))

data_of_timestamp8  = np.array(data_of_timestamp['DATA_8'])
data_of_timestamp8 = list(set(data_of_timestamp8.tolist()))

data_TOTAL_Timestamp = [data_of_timestamp1,data_of_timestamp2,data_of_timestamp3,data_of_timestamp4,data_of_timestamp5,data_of_timestamp6,data_of_timestamp7,data_of_timestamp8]

day = input("Please enter the day: ")
month = input("Please enter the month: ")
year = input("Please enter the year: ")

date_time_str = day+'/'+month+'/'+year+' '+'20:00:00'

timestamp = int(date_to_Timestamp(date_time_str))
numbers=[]
for i in range(10):
    seeds = genNUMtimestamp(timestamp,data_TOTAL_Timestamp)
    seeds_Dupli = list(set(seeds))
    while(len(seeds_Dupli)<5):
        seeds = genNUMtimestamp(timestamp,data_TOTAL_Timestamp)
        seeds_Dupli = list(set(seeds))
    tmp_arr=[]
    nums=[]
    for j in range(len(seeds)):
        np.random.seed(seeds[j])
        if(j==0):
            num=np.random.randint(1,63)
            tmp_arr.append(num)
        if(j==1):
            num=np.random.randint(2,83)
            tmp_arr.append(num)
        if(j==2):
            num=np.random.randint(4,86)
            tmp_arr.append(num)
        if(j==3):
            num=np.random.randint(9,88)
            tmp_arr.append(num)
        if(j==4):
            num=np.random.randint(14,90)
            tmp_arr.append(num)
        if(j==5):
            num=np.random.randint(26,91)
            tmp_arr.append(num)
        if(j==6):
            num=np.random.randint(1,91)
            tmp_arr.append(num)
        if(j==7) :
            num=np.random.randint(1,91)
            tmp_arr.append(num)
    for i in range(len(tmp_arr)):
        nums.append(getNumfromSEED(tmp_arr[i],i))
    numbers.append(list(set(nums)))

csvURL = 'superTICK.csv'
with open(csvURL,'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['Digit1','Digit2','Digit3','Digit4','Digit5','Digit6'])
    for i in numbers:
        myFile.writerow(i[:6])

print(f"{csvURL} file generated . . . .")