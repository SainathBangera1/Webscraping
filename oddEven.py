import random
import pandas as pd
import numpy as np
import csv
from dfunctions import date_Formater,date_Day,spitODDEVEN,duplicate,arr_string,spitPrime,prime

data = pd.read_csv("dataset.csv")
data = data[["Date","1st Digit","2nd Digit","3rd Digit","4th Digit","5th Digit","6th Digit"]]
data_Array = np.array(data)

#finding Odd and Even numbers in data sets for each date
oddEven_DATA = []

for i in data_Array:
    odd_Count=0
    even_Count=0
    primeCount=0
    nonPrimeCount=0
    tmp_arr=[]
    for y in range(1,len(i)):
        if(i[y]%2==0):
            even_Count+=1
        else:
            odd_Count+=1
    for z in range(1,len(i)):
        if(prime(i[z])==1):
            primeCount+=1
        else:
            nonPrimeCount+=1
    tmp_arr=[date_Formater(i[0]),i[1],i[2],i[3],i[4],i[5],i[6],odd_Count,even_Count,primeCount,nonPrimeCount,round((odd_Count/6)*100),round((even_Count/6)*100),round((primeCount/6)*100),round((nonPrimeCount/6)*100)]
    oddEven_DATA.append(tmp_arr)
    odd_Count=0
    even_Count=0
    tmp_arr=[]


with open("oddEven.csv","w+") as file:
    myFile = csv.writer(file)
    myFile.writerow(["Date","1st_D","2nd_D","3rd_D","4th_D","5th_D","6th_D","Odd","Even","Prime","Non_Prime","% ODD","% EVEN","% Prime","% NonPrime"])
    for i in oddEven_DATA:
        date=i[0].split('/')
        if(date_Day(date[2],date[1],date[0])=="Tuesday"):
            myFile.writerow(i)
        elif(date_Day(date[2],date[1],date[0])=="Thursday"):
            myFile.writerow(i)
        elif(date_Day(date[2],date[1],date[0])=="Saturday"):
            myFile.writerow(i)
print("Done writing oddEven.csv File.....")


#1st{1 to 14} 2nd{15 to 27} 3rd {28 to 40} 4th {41 to 53} 5th {54 to 66} 6th {67 to 90} 

oddEven_Array = spitODDEVEN(90)

num = [random.choice(oddEven_Array[0]), random.choice(oddEven_Array[0]), random.choice(
    oddEven_Array[0]), random.choice(oddEven_Array[1]), random.choice(oddEven_Array[1]), random.choice(oddEven_Array[1])]


dupli = duplicate(num)


while (len(dupli) > 0):
    for i in dupli:
        if (i == 0):
            num[i] = random.choice(oddEven_Array[0])
        elif (i == 1):
            num[i] = random.choice(oddEven_Array[0])
        elif (i == 2):
            num[i] = random.choice(oddEven_Array[0])
        elif (i == 3):
            num[i] = random.choice(oddEven_Array[1])
        elif (i == 4):
            num[i] = random.choice(oddEven_Array[1])
        elif (i == 5):
            num[i] = random.choice(oddEven_Array[1])
    dupli = duplicate(num)
num.sort()

array_toString = arr_string(num)

with open("checkNum.csv","a+") as file:
    myFile = csv.writer(file)
    myFile.writerow([array_toString])
    print("New Number inserted in check")

print(f"Stock Numbers : {num[0]},{num[1]},{num[2]},{num[3]},{num[4]},{num[5]}")

