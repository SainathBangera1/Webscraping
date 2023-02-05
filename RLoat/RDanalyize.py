import pandas as pd
import numpy as np
import csv
import json
from Rdfunctions import RDate
# Opening JSON file
file = open('./RLoat/RData.json')
  
# returns JSON object as 
# a dictionary
data_JSON = json.load(file)

data=[]

# Only 1st Set Numbers
for i in data_JSON:
    tmp=[]
    for d in RDate(i["Date"]):
        tmp.append(d)
    for l in i["fSet"]:
        tmp.append(int(l))
    data.append(tmp)

data= data[::-1]

data_Title = ['Day','Month','Year','Time']

for i in range(1,11):
    strDigit="Digit"+str(i)
    data_Title.append(strDigit)

# Even when the python file is in subfolder RLoat yet the file can be created in main folder by just giving its <filename>.csv
with open('R_FirstSET.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data:
        myFile.writerow(i)

print("Done writing R_FirstSET.csv file ...")

##########################################################################
data2=[]
# Only 2nd Set Numbers
for i in data_JSON:
    tmp=[]
    for d in RDate(i["Date"]):
        tmp.append(d)
    for l in i["sSet"]:
        tmp.append(int(l))
    data2.append(tmp)

data2= data2[::-1]

data_Title2 = ['Day','Month','Year','Time']

for i in range(1,11):
    strDigit="Digit"+str(i)
    data_Title2.append(strDigit)

# Even when the python file is in subfolder RLoat yet the file can be created in main folder by just giving its <filename>.csv
with open('R_SecondSET.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title2)
    for i in data2:
        myFile.writerow(i)

print("Done writing R_SecondSET.csv file ...")

########################################### 3 PM #####################################
data3PM=[]

for i in data:
    if i[3]==3:
        data3PM.append(i)

with open('3PM_FirstSET.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data3PM:
        myFile.writerow(i)

print("Done writing 3PM_FirstSET.csv file ...")

########################################### 4 PM #####################################
data4PM=[]

for i in data:
    if i[3]==4:
        data4PM.append(i)

with open('4PM_FirstSET.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data4PM:
        myFile.writerow(i)

print("Done writing 4PM_FirstSET.csv file ...")


########################################### 5 PM #####################################
data5PM=[]

for i in data:
    if i[3]==5:
        data5PM.append(i)


with open('5PM_FirstSET.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data5PM:
        myFile.writerow(i)

print("Done writing 5PM_FirstSET.csv file ...")


########################################### 6 PM #####################################
data6PM=[]

for i in data:
    if i[3]==6:
        data6PM.append(i)


with open('6PM_FirstSET.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data6PM:
        myFile.writerow(i)

print("Done writing 6PM_FirstSET.csv file ...")

########################################### 7 PM #####################################
data7PM=[]

for i in data:
    if i[3]==7:
        data7PM.append(i)

with open('7PM_FirstSET.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data3PM:
        myFile.writerow(i)

print("Done writing 7PM_FirstSET.csv file ...")

########################################### 8 PM #####################################
data8PM=[]

for i in data:
    if i[3]==8:
        data8PM.append(i)

with open('8PM_FirstSET.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data8PM:
        myFile.writerow(i)

print("Done writing 8PM_FirstSET.csv file ...")

######################################################################################