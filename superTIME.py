import pandas as pd
import numpy as np
import csv
import random
from dfunctions import date_to_Timestamp,findSeed


data = pd.read_csv('Superena.csv')

dataORIGINAL = np.array(data[["Day","Month","Year","Digit1","Digit2","Digit3","Digit4","Digit5","Digit6","Digit7","Digit8"]])

dataORIGINAL=dataORIGINAL.tolist()

timeSTAMPARRAY = []


for i in dataORIGINAL:
    day=i[0]
    month=i[1]
    if(i[0]<10):
        day = '0'+str(i[0])
    if(i[1]<10):
        month = '0'+str(i[1])
    day =str(i[0])
    month = str(i[1])
    year = str(i[2])
    year = year[2:]
    dateAndTime = day+'/'+month+'/'+year+' '+'20:00:00'
    timestamp = int(date_to_Timestamp(dateAndTime))
    seeds=[]
    target_Arr=i[3:]
    seeds = findSeed(timestamp,target_Arr)
    seeds.insert(0,i[0])
    seeds.insert(1,i[1])
    seeds.insert(2,i[2])
    seeds.insert(3,timestamp)
    diff1 = seeds[4]-timestamp
    seeds[4]=diff1 #1
    diff2= seeds[5] - timestamp
    seeds[5]=diff2 #2
    diff3= seeds[6] - timestamp
    seeds[6]=diff3 #3
    diff4=seeds[7] - timestamp
    seeds[7]=diff4 #4
    diff5=seeds[8] - timestamp
    seeds[8]=diff5 #5
    diff6=seeds[9]-timestamp
    seeds[9]=diff6 #6
    diff7=seeds[10]-timestamp
    seeds[10]=diff7 #7
    diff8=seeds[11]-timestamp
    seeds[11]=diff8 #8

    timeSTAMPARRAY.append(seeds)    

csvURL = 'superTime.csv'
with open(csvURL,'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['Day','Month','Year','Original','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8'])
    for i in timeSTAMPARRAY:
        myFile.writerow(i)

print("Done writing superTime.csv file  . . . . ")

########################################## DIGIT 1 #############
dataTime1 = pd.read_csv('superTime.csv')
dataTime1 = np.array(dataTime1['Digit1'])
dataTime1 = dataTime1.tolist()

dataTime1st = list(set(dataTime1))
########################################### DIGIT 2 ###########
dataTime2 = pd.read_csv('superTime.csv')
dataTime2 = np.array(dataTime2['Digit2'])
dataTime2 = dataTime2.tolist()

dataTime2nd = list(set(dataTime2))

########################################### DIGIT 3 ###########
dataTime3 = pd.read_csv('superTime.csv')
dataTime3 = np.array(dataTime3['Digit3'])
dataTime3 = dataTime3.tolist()

dataTime3rd = list(set(dataTime3))

########################################### DIGIT 4 ###########
dataTime4 = pd.read_csv('superTime.csv')
dataTime4 = np.array(dataTime4['Digit4'])
dataTime4 = dataTime4.tolist()

dataTime4th = list(set(dataTime4))

########################################### DIGIT 5 ###########
dataTime5 = pd.read_csv('superTime.csv')
dataTime5 = np.array(dataTime5['Digit5'])
dataTime5 = dataTime5.tolist()

dataTime5th = list(set(dataTime5))

########################################### DIGIT 6 ###########
dataTime6 = pd.read_csv('superTime.csv')
dataTime6 = np.array(dataTime6['Digit6'])
dataTime6 = dataTime6.tolist()

dataTime6th = list(set(dataTime6))

########################################### DIGIT 7 ###########
dataTime7 = pd.read_csv('superTime.csv')
dataTime7 = np.array(dataTime7['Digit7'])
dataTime7 = dataTime7.tolist()

dataTime7th = list(set(dataTime7))

########################################### DIGIT 8 ###########
dataTime8 = pd.read_csv('superTime.csv')
dataTime8 = np.array(dataTime8['Digit8'])
dataTime8 = dataTime8.tolist()

dataTime8th = list(set(dataTime8))


dataTIMETOTAL = [dataTime1st,dataTime2nd,dataTime3rd,dataTime4th,dataTime5th,dataTime6th,dataTime7th,dataTime8th]


# print(f"1st = {len(dataTime1st)}")
# print(f"2nd = {len(dataTime2nd)}")
# print(f"3rd = {len(dataTime3rd)}")
# print(f"4th = {len(dataTime4th)}")
# print(f"5th = {len(dataTime5th)}")
# print(f"6th = {len(dataTime6th)}")
# print(f"7th = {len(dataTime7th)}")
# print(f"8th =  {len(dataTime8th)}")

dataTIMETOTAL=[]

for i in range(len(dataTime1st)-1,331):
    dataTime1st.append(0)

for i in range(len(dataTime2nd)-1,331):
    dataTime2nd.append(0)

for i in range(len(dataTime3rd)-1,331):
    dataTime3rd.append(0)

for i in range(len(dataTime4th)-1,331):
    dataTime4th.append(0)

for i in range(len(dataTime5th)-1,331):
    dataTime5th.append(0)

for i in range(len(dataTime6th)-1,331):
    dataTime6th.append(0)

for i in range(len(dataTime8th)-1,331):
    dataTime8th.append(0)


for j in range(332):
    tmp_arr = [dataTime1st[j],dataTime2nd[j],dataTime3rd[j],dataTime4th[j],dataTime5th[j],dataTime6th[j],dataTime7th[j],dataTime8th[j]]
    dataTIMETOTAL.append(tmp_arr)

# dataTIMETOTAL = np.array(df[['DATA_1','DATA_2','DATA_3','DATA_4','DATA_5','DATA_6','DATA_7','DATA_8']])
# dataTIMETOTAL = dataTIMETOTAL.tolist()
csvURL1 = 'superUNIQUETime.csv'
with open(csvURL1,'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['DATA_1','DATA_2','DATA_3','DATA_4','DATA_5','DATA_6','DATA_7','DATA_8'])
    for i in dataTIMETOTAL:
        myFile.writerow(i)

print("Done writing superUNIQUETime.csv file  . . . . ")