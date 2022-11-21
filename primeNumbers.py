import random
import pandas as pd
import numpy as np
import csv
from dfunctions import duplicate, unionList, date_format, deltaDays, commanNumfromPairs, winNUm,prime,date_Formater
import ast

data = pd.read_csv('dataset.csv')
data = np.array(data[['Date','1st Digit','2nd Digit','3rd Digit','4th Digit','5th Digit','6th Digit']])

data_Output=[]
for i in range(len(data)):
    data[i][0] = date_Formater(data[i][0])
    tmp_arr=[data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6]]
    
    for x in range(1,7):
        tmp_arr.append(prime(data[i][x]))
    data_Output.append(tmp_arr)

data_Title = ['Date','1st Digit','2nd Digit','3rd Digit','4th Digit','5th Digit','6th Digit','1st','2nd','3rd','4th','5th','6th']

with open('prime.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data_Output:
        myFile.writerow(i)

print("Done writing prime.csv file...")

