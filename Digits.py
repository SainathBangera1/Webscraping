import pandas as pd
import numpy as np
import csv
import json

#getting data from dataset.csv using pandas
data = pd.read_csv('dataset.csv')
#converting the data in array using numpy for 1st Digit only
data1 = np.array(data[['List_Date','1st Digit']])

#Making a New Array with Day, month , year and 1st Digit
Array_1st =[]
for i in range(len(data1)):
    li = eval(data1[i][0])
    tmp_arr=[li[0],li[1],li[2],int(data1[i][1])]
    Array_1st.append(tmp_arr)

data_Title = ['Day','Month','Year','Number 1']
#writing a CSV file for 1st Digit
with open('firstArray.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in Array_1st:
        myFile.writerow(i)

print("Done Writing firstArray.csv . . .")

#####################################################################################

#converting the data in array using numpy for 2nd Digit only
data2 = np.array(data[['List_Date','2nd Digit']])

#Making a New Array with Day, month , year and 2nd Digit
Array_2nd =[]
for i in range(len(data2)):
    li = eval(data2[i][0])
    tmp_arr=[li[0],li[1],li[2],int(data2[i][1])]
    Array_2nd.append(tmp_arr)

data_Title = ['Day','Month','Year','Number 2']
#writing a CSV file for 1st Digit
with open('secondArray.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in Array_2nd:
        myFile.writerow(i)

print("Done Writing secondArray.csv . . .")

#############################################################################

#converting the data in array using numpy for 3rd Digit only
data3 = np.array(data[['List_Date','3rd Digit']])

#Making a New Array with Day, month , year and 3rf Digit
Array_3rd =[]
for i in range(len(data3)):
    li = eval(data3[i][0])
    tmp_arr=[li[0],li[1],li[2],int(data3[i][1])]
    Array_3rd.append(tmp_arr)

data_Title = ['Day','Month','Year','Number 3']
#writing a CSV file for 1st Digit
with open('thirdArray.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in Array_3rd:
        myFile.writerow(i)

print("Done Writing thirdArray.csv . . .")

#########################################################################

#converting the data in array using numpy for 4th Digit only
data4 = np.array(data[['List_Date','4th Digit']])

#Making a New Array with Day, month , year and 4th Digit
Array_4th =[]
for i in range(len(data4)):
    li = eval(data4[i][0])
    tmp_arr=[li[0],li[1],li[2],int(data4[i][1])]
    Array_4th.append(tmp_arr)

data_Title = ['Day','Month','Year','Number 4']
#writing a CSV file for 1st Digit
with open('fourthArray.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in Array_4th:
        myFile.writerow(i)

print("Done Writing fourthArray.csv . . .")

#########################################################################

#converting the data in array using numpy for 5th Digit only
data5 = np.array(data[['List_Date','5th Digit']])

#Making a New Array with Day, month , year and 5th Digit
Array_5th =[]
for i in range(len(data5)):
    li = eval(data5[i][0])
    tmp_arr=[li[0],li[1],li[2],int(data5[i][1])]
    Array_5th.append(tmp_arr)

data_Title = ['Day','Month','Year','Number 5']
#writing a CSV file for 1st Digit
with open('fifthArray.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in Array_5th:
        myFile.writerow(i)

print("Done Writing fifthArray.csv . . .")

#########################################################################

#converting the data in array using numpy for 6th Digit only
data6 = np.array(data[['List_Date','6th Digit']])

#Making a New Array with Day, month , year and 6th Digit
Array_6th =[]
for i in range(len(data6)):
    li = eval(data6[i][0])
    tmp_arr=[li[0],li[1],li[2],int(data6[i][1])]
    Array_6th.append(tmp_arr)

data_Title = ['Day','Month','Year','Number 6']
#writing a CSV file for 1st Digit
with open('sixthArray.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in Array_6th:
        myFile.writerow(i)

print("Done Writing sixthArray.csv . . .")