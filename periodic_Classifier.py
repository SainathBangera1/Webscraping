import pandas as pd
import numpy as np
import csv
import json

# Opening JSON file
file = open('periodicTable.json')
  
# returns JSON object as 
# a dictionary
data_JSON = json.load(file)

data = pd.read_csv('dataset.csv')
data = np.array(data[['Date','1st Digit','2nd Digit','3rd Digit','4th Digit','5th Digit','6th Digit']])
dataAMU = data
for i in range(len(data)):
    for j in range(len(data[i])):
        for k,v in data_JSON.items():
            if(int(k)==data[i][j]):
                data[i][j]=v["SYMBOL"]
    ##### Dont use single for loop for SYMBOL AND AMU otherwise their will be key error            
    for l in range(len(data[i])):
        for k,v in data_JSON.items():
            if(int(k)==data[i][l]):
                dataAMU[i][l]=v["AMU"]    


data_Title = ['Date','1st Digit','2nd Digit','3rd Digit','4th Digit','5th Digit','6th Digit']

with open('periodicName_Dataset.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data:
        myFile.writerow(i)

print("Done Writing periodicName_Dataset.csv . . .")

with open('periodicAMU_Dataset.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in dataAMU:
        myFile.writerow(i)

print("Done Writing periodicAMU_Dataset.csv . . . ")
