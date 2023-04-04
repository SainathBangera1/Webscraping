import pandas as pd
import numpy as np
import csv
import random
from dfunctions import reApfunction

data = pd.read_csv('superTime.csv')

data1st = np.array(data[["Original","Digit1"]])
data2nd = np.array(data[["Original","Digit2"]])
data3rd = np.array(data[["Original","Digit3"]])
data4th = np.array(data[["Original","Digit4"]])
data5th = np.array(data[["Original","Digit5"]])
data6th = np.array(data[["Original","Digit6"]])
##################################################################
data2 = pd.read_csv('superUNIQUETime.csv')
data2_1st = np.array(data2["DATA_1"])
data2_1st = data2_1st[:271]
data2_2nd= np.array(data2["DATA_2"])
data2_2nd = data2_2nd[:311]
data2_3rd= np.array(data2["DATA_3"])
data2_3rd = data2_3rd[:312]
data2_4th= np.array(data2["DATA_4"])
data2_4th = data2_4th[:305]
data2_5th= np.array(data2["DATA_5"])
data2_5th = data2_5th[:289]
data2_6th= np.array(data2["DATA_6"])
data2_6th = data2_6th[:271]

# the data2 has unique data points hence i will take it in the main array
# based on data2 i will check each element in data which has that value
# and then make a seperate array consisting timestamp for each data points 
# the above procedure will be followed digit wise

#data_1st array is for the 1st Digit position
data_1st=[]
for i in data2_1st:
    tmp_arr=[]
    for j in data1st:
        if(i==j[1]):
            tmp_arr.append(j[0])
    data_1st.append([i,tmp_arr])

#data2nd array is for the 2nd Digit position
data_2nd=[]
for i in data2_2nd:
    tmp_arr=[]
    for j in data2nd:
        if(i==j[1]):
            tmp_arr.append(j[0])
    data_2nd.append([i,tmp_arr])

#data3rd array is for the 3rd Digit position
data_3rd=[]
for i in data2_3rd:
    tmp_arr=[]
    for j in data3rd:
        if(i==j[1]):
            tmp_arr.append(j[0])
    data_3rd.append([i,tmp_arr])

#data4th array is for the 4th Digit position
data_4th=[]
for i in data2_4th:
    tmp_arr=[]
    for j in data4th:
        if(i==j[1]):
            tmp_arr.append(j[0])
    data_4th.append([i,tmp_arr])


#data5th array is for the 5th Digit position
data_5th=[]
for i in data2_5th:
    tmp_arr=[]
    for j in data5th:
        if(i==j[1]):
            tmp_arr.append(j[0])
    data_5th.append([i,tmp_arr])

#data6th array is for the 5th Digit position
data_6th=[]
for i in data2_6th:
    tmp_arr=[]
    for j in data6th:
        if(i==j[1]):
            tmp_arr.append(j[0])
    data_6th.append([i,tmp_arr])

# reApfunction(data_6th[0][1],1)