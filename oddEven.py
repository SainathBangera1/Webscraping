import random
import pandas as pd
import numpy as np
import csv
from dfunctions import date_Formater,date_Day

data = pd.read_csv("dataset.csv")
data = data[["Date","1st Digit","2nd Digit","3rd Digit","4th Digit","5th Digit","6th Digit"]]
data_Array = np.array(data)

#finding Odd and Even numbers in data sets for each date
oddEven_DATA = []

for i in data_Array:
    odd_Count=0
    even_Count=0
    tmp_arr=[]
    for y in range(1,len(i)):
        if(i[y]%2==0):
            even_Count+=1
        else:
            odd_Count+=1
    tmp_arr=[date_Formater(i[0]),i[1],i[2],i[3],i[4],i[5],i[6],odd_Count,even_Count,(odd_Count/6)*100,(even_Count/6)*100]
    oddEven_DATA.append(tmp_arr)
    odd_Count=0
    even_Count=0
    tmp_arr=[]

with open("oddEven.csv","w+") as file:
    myFile = csv.writer(file)
    myFile.writerow(["Date","1st_D","2nd_D","3rd_D","4th_D","5th_D","6th_D","Odd","Even","% ODD","% /EVEN"])
    for i in oddEven_DATA:
        date=i[0].split('/')
        if(date_Day(date[2],date[1],date[0])=="Tuesday"):
            myFile.writerow(i)
        elif(date_Day(date[2],date[1],date[0])=="Thursday"):
            myFile.writerow(i)
        elif(date_Day(date[2],date[1],date[0])=="Saturday"):
            myFile.writerow(i)
print("Done writing oddEven.csv File.....")