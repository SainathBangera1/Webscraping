import matplotlib.pyplot as plt
import ast
import numpy as np
import pandas as pd
import csv
import sys
import matplotlib
from dfunctions import date_format,deltaDays,prime,sub,trials,factorizor



data = pd.read_csv('dataset.csv')
data = np.array(data[['List_Date', '1st Digit', '2nd Digit',
                '3rd Digit', '4th Digit', '5th Digit', '6th Digit']])

# to get first appearance date for all Numbers

first_Date_Apperance = []

for i in range(1, 91):
    for x in data:
        if i in [x[1], x[2], x[3], x[4], x[5], x[6]]:
            first_Date_Apperance.append([i,date_format(ast.literal_eval(x[0]))])
            break

for y in first_Date_Apperance:
    for z in data:
        if y[0] in [z[1], z[2], z[3], z[4], z[5], z[6]]:
            ldate=date_format(ast.literal_eval(z[0]))
            y.append(deltaDays(ldate,y[1]))


max_Delta_points = []
for z in first_Date_Apperance:
    max_Delta_points.append(len(z[2:]))

MAX_DELTA_PRIME=max(max_Delta_points)
# print(max_Delta_points)
# print(f"Length of Max delta points: {len(max_Delta_points)}")
# print(MAX_DELTA_PRIME)

prime_DELTA_TITLE = ["Ball Num","Start_date"]

for i in range(1,MAX_DELTA_PRIME+1):
    str_tmp = "Point "+str(i)
    prime_DELTA_TITLE.append(str_tmp)
    str_tmp=''

with open("prime_DELTA.csv","w+") as file:
    myFile = csv.writer(file)
    myFile.writerow(prime_DELTA_TITLE)
    for i in first_Date_Apperance:
        myFile.writerow(i)

print("Done Writing prime_DELTA.csv file...... ")

data_New = pd.read_csv('prime_DELTA.csv')
data_New = data_New.replace('NaN', np.nan)
data_New = data_New.fillna(0)
data_Set = np.array(data_New)
data_Set = data_Set[0][3:]

data_Set_arr = []

prime_ARRAY = []

for i in data_Set:
    if prime(int(i))==0:
        data_Set_arr.append([i,0,factorizor(int(i))])
    else:
        if(int(i)!=0):
            prime_ARRAY.append(int(i))
            data_Set_arr.append([i,1])

with open('1st_Digit_delta.csv','w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['delta','Prime','Last factor'])
    for i in data_Set_arr:
        myFile.writerow(i)

print("Done Writing 1st_Digit_delta.csv .....")




# print(prime_ARRAY)

# prime_Difference=[]

# for i in range(len(prime_ARRAY)):
#     if(i+1 < len(prime_ARRAY)):
#         prime_Difference.append(sub(prime_ARRAY[i+1],prime_ARRAY[i]))

# prime_inBetween=[]
# for i in range(4657,4910):
#     if(prime(i)==1):
#         prime_inBetween.append(i)

# print(len(prime_inBetween)-2)

