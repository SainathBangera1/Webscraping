import pandas as pd
import numpy as np
import csv
import random
from dfunctions import dictFreq,odds,primes,sepratePrimes,seprateNonPrimes,duplicate,spitZero,prime

time = input("Please enter the time in PM: ")
csvURL = time+'PM_Combined.csv'
#KENO DATA
dataOg = pd.read_csv(csvURL)
data = np.array(dataOg[['Day','Month','Year','Time','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10','Digit11','Digit12','Digit13','Digit14','Digit15','Digit16','Digit17','Digit18','Digit19','Digit20']])
newData=[]
for i in data:
    if (i[3]!=0):
        newData.append(i)

primeData=[]

for j in newData:
    dta = primes(j[4:len(j)])
    primeData.append(dta)

primeCount=[]
nonPrimeCount = []

for k in primeData:
    primeCount.append(k[0])
    nonPrimeCount.append(k[1])

print(f"Primes in a row minimum: {max(primeCount)} %")
print(f"NonPrimes in a row minimum: {max(nonPrimeCount)} %")

#IN a row their are minimum ZERO prime numbers and then 5 prime numbers occured only in One day


