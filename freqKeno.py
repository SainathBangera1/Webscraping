import pandas as pd
import numpy as np
import csv
import random
from dfunctions import matchNum,prime,frequency,generateMODEL1,next_number,spitZero




print("Following are the model names of csv file available")
print("1. 4PM_Combined.csv")
print("2. 5PM_Combined.csv")
print("3. 6PM_Combined.csv")
print("4. 7PM_Combined.csv")
print("5. 8PM_Combined.csv")

time = input("Enter the timeset of Data that you want from above options: ")

csvURL = time+'PM_Combined.csv'

data = pd.read_csv(csvURL)
data1 = np.array(data[["Day","Month","Year","Digit1","Digit2","Digit3","Digit4","Digit5","Digit6","Digit7","Digit8","Digit9","Digit10","Digit11","Digit12","Digit13","Digit14","Digit15","Digit16","Digit17","Digit18","Digit19","Digit20"]])

digit1=np.array(data["Digit1"])
digit1=spitZero(digit1)









# primeArr=[]
# nonPrimeArr = []

# for i in range(1,81):
#     if(prime(i)==1):
#         primeArr.append(i)
#     else:
#         nonPrimeArr.append(i)

# frequencyData=[]

# for i in nonPrimeArr:
#     count=0
#     for j in data:
#         if(i in j):
#             count+=1
#     frequencyData.append([i,count])

# minFreq=[]
# total=0
# firstNum=[]
# secondNum=[]
# count=0
# for i in frequencyData:
#     firstNum.append(i[0])

#avg = total/len(minFreq)
# print(min(minFreq))
# print(max(minFreq))
# print(f"Average : {avg}")
# print(f"Numbers total : {len(catchNum)}")
# print(catchNum)
# print(len(frequencyData))

# num = []
# genNum=[]
# for i in range(20):
#     for j in range(3):
#         genNum=generateMODEL1(firstNum)
#     num.append(genNum)

# csvURL2 = time+'pmKENO.csv'
# with open(csvURL2,'w+') as file:
#     myFile = csv.writer(file)
#     myFile.writerow(['Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10'])
#     for i in num:
#         myFile.writerow(i)

# print(f"{csvURL2} file generated . . . .")