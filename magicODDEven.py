import pandas as pd
import numpy as np
import csv
import random
from dfunctions import prime,generateNum,compareList,delElements,delElements1

#Magic DATA
dataONE = pd.read_csv('Magic.csv')

data = np.array(dataONE[['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5']])


for i in range(len(data)):
    for j in range(3,8):
        if(prime(data[i][j])==1):
            data[i][j]=1
        elif(prime(data[i][j])==0):
            data[i][j]=0

with open('magicODDEVEN.csv','w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5'])
    for i in data:
        myFile.writerow(i)

print("Done writing magicODDEVEN,csv file . . .")

# ################################################################################################

dataTWO = pd.read_csv('magicODDEVEN.csv')

data2 = np.array(dataTWO[['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5']])

oddEveArr = []

for i in data2:
    total = i[3]+i[4]+i[5]+i[6]+i[7]
    prime_percentage = round((total/6)*100)
    oddEveArr.append([prime_percentage,100-prime_percentage])

count=0
count2=0
for j in oddEveArr:
    count+=j[0]
    count2+=j[1]

# print(f"Primes Average: {round(count/len(oddEveArr))} %")
# print(f"NON Primes Average: {round(count2/len(oddEveArr))} %")

# Prime Average = 29%
# Non Prime Average = 71 %

primeNums =[]
nonPrimeNums = []

for i in range(1,38):
    if(prime(i)==1):
        primeNums.append(i)
    else:
        nonPrimeNums.append(i)

predicated=[]
countNUM=0

ar1 = np.copy(primeNums)
ar2 = np.copy(nonPrimeNums)

while (countNUM!=15):
    num_arr = generateNum(ar1,ar2)
    countNUM+=1
    ar1= delElements(num_arr,ar1,primeNums)
    ar2= delElements1(num_arr,ar2,nonPrimeNums)
    predicated.append(num_arr)

with open('magic2_generated.csv','a+') as file:
    myFile = csv.writer(file)
    for i in predicated:
        myFile.writerow(i)

print("10 nums generated in magic2_generated.csv")
