import pandas as pd
import numpy as np
import csv
import random
from dfunctions import dictFreq,odds,primes,sepratePrimes,seprateNonPrimes,duplicate,spitZero,prime,generateMODEL1,delElements,delElements1,generateMODEL2


time = input("Please enter the time in PM: ")
csvURL = time+'PM_Combined.csv'
#KENO DATA
dataOg = pd.read_csv(csvURL)
data = np.array(dataOg[['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10','Digit11','Digit12','Digit13','Digit14','Digit15','Digit16','Digit17','Digit18','Digit19','Digit20']])

newData = []

#removing all the Missing dates ZERO Values and storing the filtered value in newData Array
for i in data:
    if(i[3]!=0):
        newData.append(i)

data = np.copy(newData)

primeNums = []
nonPrimesNums =[]

for i in range(1 ,81):
    if(prime(i)==1):
        primeNums.append(i)
    else:
        nonPrimesNums.append(i)

# 4 primes , 6 non Primes combinations
# 7 primes , 3 non Primes combinations
# 3 primes , 7 non Primes combinations


# ############################### 1ST MODEL - 4 PRIME , 6 NON-PRIME

ar1 = np.copy(primeNums)
ar2 = np.copy(nonPrimesNums)
predicated = []
countNUM = 0
while (countNUM!=10):
    num_arr = generateMODEL1(ar1,ar2)
    countNUM+=1
    # ar1= delElements(num_arr,ar1,primeNums)
    # ar2= delElements1(num_arr,ar2,nonPrimesNums)
    predicated.append(num_arr)
csvURL1='modelONE'+time+'PM.csv'
with open(csvURL1,'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10'])
    for i in predicated:
        myFile.writerow(i)

print(f"10 nums generated in modelONE{time}PM.csv")

# ############################### 2ND MODEL - 7 PRIME , 3 NON-PRIME

ar1 = np.copy(primeNums)
ar2 = np.copy(nonPrimesNums)
predicated = []
countNUM = 0
while (countNUM!=10):
    num_arr = generateMODEL2(ar1,ar2)
    countNUM+=1
    # ar1= delElements(num_arr,ar1,primeNums)
    # ar2= delElements1(num_arr,ar2,nonPrimesNums)
    predicated.append(num_arr)

csvURL2='modelTWO'+time+'PM.csv'
with open(csvURL2,'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10'])
    for i in predicated:
        myFile.writerow(i)

print(f"10 nums generated in modelTWO{time}PM.csv")