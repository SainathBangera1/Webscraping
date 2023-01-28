import pandas as pd
import numpy as np
import csv
from dfunctions import sortString,removeDuplicate,lisToDate

#getting data from dataset.csv using pandas
data = pd.read_csv('dataset.csv')
#converting the data in array using numpy
data = np.array(data[['List_Date','1st Digit','2nd Digit','3rd Digit','4th Digit','5th Digit','6th Digit']])

#Creating a New Array to Store value in csv file
Array_Num_Strings = []
#converting all digits to string and then adding them up
for i in range(len(data)):
    tmp_arr=[data[i][0]]
    strNum = str(data[i][1])+str(data[i][2])+str(data[i][3])+str(data[i][4])+str(data[i][5])+str(data[i][6])
    # Driver code
    strResult = sortString(strNum)
    tmp_arr.append(strResult)
    Array_Num_Strings.append(tmp_arr)

data_Title = ['List_Date','Str_Nums']
#writing a CSV file for 1st Digit
with open('strNums.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in Array_Num_Strings:
        myFile.writerow(i)

print("Done Writing strNums.csv . . .")

unique_Arr=[]
#finding the duplicates in Array_Num_Strings
for i in Array_Num_Strings:
    #removeDuplicate function hels to eliminate duplicate numbers within
    #input = '113333444567' output = 134567
    unique_Arr.append(sortString(removeDuplicate(i[1])))
unique_Arr=list(set(unique_Arr))    

#new_Array_Num_Strings is an new array to store the nonDuplicate values within string for each date
new_Array_Num_Strings=[]
for i in Array_Num_Strings:
    tmp_arr=[eval(i[0]),sortString(removeDuplicate(i[1]))]
    new_Array_Num_Strings.append(tmp_arr)


#checking the Unique number Frequency
uniqueFreq_Arr=[]
for i in unique_Arr:
    tmp_arr=[]
    count=0
    for j in new_Array_Num_Strings:
        if (j[1]==i):
            count+=1
    tmp_arr.append(i)
    tmp_arr.append(count)
    uniqueFreq_Arr.append(tmp_arr)


#Frequency of Unique number and Dates

uniFreqDate=[]

for i in uniqueFreq_Arr:
    tmp_arr=[]
    for j in new_Array_Num_Strings:
        if(j[1]==i[0]):
            tmp_arr.append(lisToDate(j[0]))
    tmp_str='@'+str(i[0])
    dataFUD=[tmp_str,i[1],tmp_arr] #dataFUD = [Unique Number, Frequency, Array of Dates ]
    uniFreqDate.append(dataFUD)

#writing Unique Frequency array in CSV file
data_Title = ['Unique Number', 'Frequency', 'Array of Dates' ]
#writing a CSV file for 1st Digit
with open('FUD.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in uniFreqDate:
        myFile.writerow(i)

print("Done Writing FUD.csv . . .")