import pandas as pd
import numpy as np
import csv
import random
from dfunctions import verticalFreq,prime,spitZero,primes,sepratePrimes,seprateNonPrimes,generateNum,checkit,superenaNum


data = pd.read_csv('Superena.csv')

digitsArray=[]

dataORIGINAL=[]

dataORIGINAL1 = np.array(data[["Day","Month","Year","Digit1","Digit2","Digit3","Digit4","Digit5","Digit6"]])


dataORIGINAL=dataORIGINAL1.tolist()


for i in range(1,7):
    element='Digit'+str(i)
    arrElement = np.array(data[element])
    digitsArray.append(arrElement)

choiceArray=[]
choiceArray1=[]
indexofChoice=0
for j in range(len(digitsArray)):
    resultPrimeNonPrime = list(set(digitsArray[j]))
    choiceArray.append(resultPrimeNonPrime)
    primeNumbers = sepratePrimes([],resultPrimeNonPrime)
    if(indexofChoice>=2):
        nonPrimeNumbers = seprateNonPrimes([],resultPrimeNonPrime)
        choiceArray1.append(nonPrimeNumbers)
    else:
        choiceArray1.append(resultPrimeNonPrime)
    #choiceArray.append(nonPrimeNumbers)
    # print(f"{choiceArray1[indexofChoice]}")
    #print(f"Digit {j+1} ==> Range ({min(digitsArray[j])} to {max(digitsArray[j])}) , Number of Elements -> {len(resultPrimeNonPrime)} , Non Primes -> {len(nonPrimeNumbers)} , {round((len(nonPrimeNumbers)/len(resultPrimeNonPrime))*100)} %")
    indexofChoice+=1
    # print(f"Digit {j+1} ==> Range ({min(digitsArray[j])} to {max(digitsArray[j])}) , Non Primes -> {len(nonPrimeNumbers)}")
    # print(resultPrimeNonPrime)

#row wise distribution of primes and non primes

# data2 = np.array(data[["Digit1","Digit2","Digit3","Digit4","Digit5","Digit6"]])
# count=0
# nonPrimeArr=[]
# for i in data2:
#     for j in i:
#         if(prime(j)==0):
#             count+=1
#     nonPrimeArr.append(round((count/6)*100))
#     count=0

# print(f"Minimum Non Primes in a row {min(nonPrimeArr)} %")
# print(f"Maximum Non Primes in a row {max(nonPrimeArr)} %")
# print(f"Average Non Primes {round(sum(nonPrimeArr)/len(nonPrimeArr))} %")

################################## ANALYSIS OF SUPERENA DATA SET #######################################
# Digit 1 ==> Range (1 to 65) , Number of Elements -> 60 , Non Primes -> 41 , 68 %
# Digit 2 ==> Range (2 to 82) , Number of Elements -> 71 , Non Primes -> 51 , 72 %
# Digit 3 ==> Range (4 to 85) , Number of Elements -> 79 , Non Primes -> 58 , 73 %
# Digit 4 ==> Range (9 to 87) , Number of Elements -> 79 , Non Primes -> 60 , 76 %
# Digit 5 ==> Range (14 to 89) , Number of Elements -> 73 , Non Primes -> 55 , 75 %
# Digit 6 ==> Range (26 to 90) , Number of Elements -> 57 , Non Primes -> 44 , 77 %
# Minimum Non Primes in a row 17 %
# Maximum Non Primes in a row 100 %
# Average Non Primes 73 %

######## 1st Digit
firstDigitFrequency=[]
for i in choiceArray[0]:
    count=0
    for j in digitsArray[0]:
        if(i==j):
            count+=1
    firstDigitFrequency.append([i,count])
    count=0

######## 2nd Digit
secondDigitFrequency=[]
for i in choiceArray[1]:
    count=0
    for j in digitsArray[1]:
        if(i==j):
            count+=1
    secondDigitFrequency.append([i,count])
    count=0

######## 3rd Digit
thirdDigitFrequency=[]
for i in choiceArray[2]:
    count=0
    for j in digitsArray[2]:
        if(i==j):
            count+=1
    thirdDigitFrequency.append([i,count])
    count=0

######## 4th Digit
fourthDigitFrequency=[]
for i in choiceArray[3]:
    count=0
    for j in digitsArray[3]:
        if(i==j):
            count+=1
    fourthDigitFrequency.append([i,count])
    count=0

######## 5th Digit
fifthDigitFrequency=[]
for i in choiceArray[4]:
    count=0
    for j in digitsArray[4]:
        if(i==j):
            count+=1
    fifthDigitFrequency.append([i,count])
    count=0

######## 6th Digit
sixthDigitFrequency=[]
for i in choiceArray[5]:
    count=0
    for j in digitsArray[5]:
        if(i==j):
            count+=1
    sixthDigitFrequency.append([i,count])
    count=0

totalperDigitfrequency=[]
for i in range(1,91):
    totalperDigitfrequency.append([i])

totalperDigitfrequency=verticalFreq(firstDigitFrequency,totalperDigitfrequency)
for i in totalperDigitfrequency:
    if(len(i)==1):
        i.append(0)

totalperDigitfrequency=verticalFreq(secondDigitFrequency,totalperDigitfrequency)
for i in totalperDigitfrequency:
    if(len(i)==2):
        i.append(0)

totalperDigitfrequency=verticalFreq(thirdDigitFrequency,totalperDigitfrequency)
for i in totalperDigitfrequency:
    if(len(i)==3):
        i.append(0)

totalperDigitfrequency=verticalFreq(fourthDigitFrequency,totalperDigitfrequency)
for i in totalperDigitfrequency:
    if(len(i)==4):
        i.append(0)

totalperDigitfrequency=verticalFreq(fifthDigitFrequency,totalperDigitfrequency)
for i in totalperDigitfrequency:
    if(len(i)==5):
        i.append(0)

totalperDigitfrequency=verticalFreq(sixthDigitFrequency,totalperDigitfrequency)
for i in totalperDigitfrequency:
    if(len(i)==6):
        i.append(0)

percentDigitFreq=[]
for i in totalperDigitfrequency:
    digit1=round((i[1]/sum(i[1:]))*100,2)
    digit2=round((i[2]/sum(i[1:]))*100,2)
    digit3=round((i[3]/sum(i[1:]))*100,2)
    digit4=round((i[4]/sum(i[1:]))*100,2)
    digit5=round((i[5]/sum(i[1:]))*100,2)
    digit6=round((i[6]/sum(i[1:]))*100,2)
    percentDigitFreq.append([i[0],digit1,digit2,digit3,digit4,digit5,digit6])


csvURL = 'superVERTICAL.csv'
with open(csvURL,'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['Ball','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6'])
    for i in totalperDigitfrequency:
        myFile.writerow(i)

print("Done writing superVERTICAL.csv file  . . . . ")

csvURL2 = 'superPERCENT_VERTICAL.csv'
with open(csvURL2,'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['Ball','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6'])
    for i in percentDigitFreq:
        myFile.writerow(i)

print("Done writing superPERCENT_VERTICAL.csv file  . . . . ")

############## Probabilty of verticals in horizontals
    

for i in percentDigitFreq:
    for j in dataORIGINAL:
        if(i[0] in j[3:]):
            indexElement=j[3:].index(i[0],0,len(j[3:]))
            if(indexElement==0):
                j[indexElement+3]=i[1]
            elif(indexElement==1):
                j[indexElement+3]=i[2]
            elif(indexElement==2):
                j[indexElement+3]=i[3]
            elif(indexElement==3):
                j[indexElement+3]=i[4]
            elif(indexElement==4):
                j[indexElement+3]=i[5]
            elif(indexElement==5):
                j[indexElement+3]=i[6]

csvURL3 = 'superPERCENT_HORIZONTAL.csv'
with open(csvURL3,'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6'])
    for i in dataORIGINAL:
        myFile.writerow(i)

print("Done writing superPERCENT_HORIZONTAL.csv file  . . . . ")

# for i in firstDigitFrequency:
#     for j in totalperDigitfrequency:
#         if(i[0]==j[0]):
#             j.append(i[1])




############################################### TICKETS AMOUNT ###################################
# tickets=[]

# for i in range(10):
#     superNum=[]
#     for i in range(587):
#         superNum = superenaNum(choiceArray[0],choiceArray[1],choiceArray[2],choiceArray[3],choiceArray[4],choiceArray[5])
#     tickets.append(superNum)


# csvURL = 'superTICKETS.csv'
# with open(csvURL,'w+') as file:
#     myFile = csv.writer(file)
#     myFile.writerow(['Digit1','Digit2','Digit3','Digit4','Digit5','Digit6'])
#     for i in tickets:
#         myFile.writerow(i)

# print(f"{csvURL} file generated . . . .")