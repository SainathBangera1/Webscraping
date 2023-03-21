import pandas as pd
import numpy as np
import csv
import random
from dfunctions import prime,spitZero,primes,sepratePrimes,seprateNonPrimes,generateNum,checkit


print("Following are the model names of csv file available")
print("1. 4PM_Combined.csv")
print("2. 5PM_Combined.csv")
print("3. 6PM_Combined.csv")
print("4. 7PM_Combined.csv")
print("5. 8PM_Combined.csv")

time = input("Enter the timeset of Data that you want from above options: ")

csvURL = time+'PM_Combined.csv'

data = pd.read_csv(csvURL)

digitsArray=[]

#data = np.array(data[["Digit1","Digit2","Digit3","Digit4","Digit5","Digit6","Digit7","Digit8","Digit9","Digit10","Digit11","Digit12","Digit13","Digit14","Digit15","Digit16","Digit17","Digit18","Digit19","Digit20"]])

for i in range(1,21):
    element='Digit'+str(i)
    arrElement = np.array(data[element])
    arrElement = spitZero(arrElement)
    digitsArray.append(arrElement)

choiceArray=[]
indexofChoice=0
for j in range(len(digitsArray)):
    resultPrimeNonPrime = list(set(digitsArray[j]))
    primeNumbers = sepratePrimes([],resultPrimeNonPrime)
    nonPrimeNumbers = seprateNonPrimes([],resultPrimeNonPrime)
    choiceArray.append(resultPrimeNonPrime)
    #choiceArray.append(nonPrimeNumbers)
    # print(f"{choiceArray[indexofChoice]}")
    # print(f"Digit {j+1} ==> Range ({min(digitsArray[j])} to {max(digitsArray[j])}) , Number of Elements -> {len(resultPrimeNonPrime)} , Non Primes -> {len(nonPrimeNumbers)}")
    # indexofChoice+=1
    # print(f"Digit {j+1} ==> Range ({min(digitsArray[j])} to {max(digitsArray[j])}) , Non Primes -> {len(nonPrimeNumbers)}")
    # print(resultPrimeNonPrime)


num = []
# ORIGINAL_CHOICE_ARR = np.copy(choiceArray)
for i in range(50):
    # genNormal=generateNum(a,a,a,a,a,a,a,a,a,a)
    # num.append(genNormal)
    # genNum=generateNum(choiceArray[0],choiceArray[1],choiceArray[10],choiceArray[14],choiceArray[9],choiceArray[15],choiceArray[16],choiceArray[11],choiceArray[13],choiceArray[19])
    # num.append(genNum)
    # genNum1=generateNum(choiceArray[0],choiceArray[1],choiceArray[2],choiceArray[3],choiceArray[4],choiceArray[5],choiceArray[6],choiceArray[7],choiceArray[8],choiceArray[9])
    # genNum2=generateNum(choiceArray[10],choiceArray[11],choiceArray[12],choiceArray[13],choiceArray[14],choiceArray[15],choiceArray[16],choiceArray[17],choiceArray[18],choiceArray[19])
    for i in range(3):
        genNum1=generateNum(choiceArray[0],choiceArray[1],choiceArray[2],choiceArray[3],choiceArray[4],choiceArray[5],choiceArray[6],choiceArray[7],choiceArray[8],choiceArray[9]) 
    num.append(genNum1)
    for j in range(9):
        genNum2=generateNum(choiceArray[10],choiceArray[11],choiceArray[12],choiceArray[13],choiceArray[14],choiceArray[15],choiceArray[16],choiceArray[17],choiceArray[18],choiceArray[19])
    num.append(genNum2)
    # combineArr = list(set(genNum1).union(set(genNum2)))
    #print(len(combineArr)) 
    #num.append(generateMODEL2(combineArr))


csvURL2 = time+'pmKENORANGE.csv'
with open(csvURL2,'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10'])
    for i in num:
        myFile.writerow(i)

print(f"{csvURL2} file generated . . . .")