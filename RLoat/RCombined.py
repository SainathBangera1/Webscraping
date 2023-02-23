import pandas as pd
import numpy as np
import csv
import json
from Rdfunctions import RDate,checkDate
# Opening JSON file
file = open('./RLoat/RData.json')
  
# returns JSON object as 
# a dictionary
data_JSON = json.load(file)

count=0

data=[]

# 20 of Set Numbers
for i in data_JSON:
    tmp=[]
    for d in RDate(i["Date"]):
        tmp.append(d)
    for l in i["fSet"]:
        tmp.append(int(l))
    for m in i["sSet"]:
        tmp.append(int(m))
    data.append(str(tmp))

data = set(data)
tmp1=[]
for i in data:
    arr = eval(i)
    tmp1.append(arr)

data=tmp1

newData = []

for i in range(2020,2024):
    for j in range(1,13):
        for k in range(1,32):
            for l in data:
                if(l[2]==i and l[1]==j and l[0]==k):
                    newData.append(l)
                else:
                    pass

missing_Arr=[]
for i in range(len(newData)):
    tmp_arr=[]
    if(i+1<len(newData)):
        if(newData[i][2]==newData[i+1][2]):
            if(newData[i][1]==newData[i+1][1]):
                if((newData[i+1][0]-newData[i][0])>1):
                    rg =newData[i+1][0]-newData[i][0]
                    for j in range(1,rg):
                        day = newData[i][0]+j
                        month=newData[i][1]
                        year=newData[i][2]
                        tmp_arr = [day,month,year,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        missing_Arr.append([i,tmp_arr])

missing_Arr = missing_Arr[::-1]
for j in missing_Arr:
    newData.insert(j[0],j[1])
    # print(newData[j[0]])

data = newData
data_Title = ['Day','Month','Year','Time']

for i in range(1,21):
    strDigit="Digit"+str(i)
    data_Title.append(strDigit)

# Even when the python file is in subfolder RLoat yet the file can be created in main folder by just giving its <filename>.csv
with open('keno.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data:
        myFile.writerow(i)

print("Done writing keno.csv file ...")


data4PM=[]

for i in data:
    if i[3]==4 or i[3]==0:
        data4PM.append(i)

with open('4PM_Combined.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data4PM:
        myFile.writerow(i)

print("Done writing 4PM_Combined.csv file ...")



data5PM=[]

for i in data:
    if i[3]==5 or i[3]==0:
        data5PM.append(i)

with open('5PM_Combined.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data5PM:
        myFile.writerow(i)

print("Done writing 5PM_Combined.csv file ...")

data6PM=[]

for i in data:
    if i[3]==6 or i[3]==0:
        data6PM.append(i)

with open('6PM_Combined.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data6PM:
        myFile.writerow(i)

print("Done writing 6PM_Combined.csv file ...")

data7PM=[]

for i in data:
    if i[3]==7 or i[3]==0:
        data7PM.append(i)

with open('7PM_Combined.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data7PM:
        myFile.writerow(i)

print("Done writing 7PM_Combined.csv file ...")

data8PM=[]

for i in data:
    if i[3]==8 or i[3]==0:
        data8PM.append(i)

with open('8PM_Combined.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data8PM:
        myFile.writerow(i)

print("Done writing 8PM_Combined.csv file ...")