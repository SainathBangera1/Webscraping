from bs4 import BeautifulSoup
from dfunctions import periodic
import json
import re
import csv

data_Test=[]
data_Test2=[]
data_Test3={}

HTMLFileToBeOpened = open('htmlData/periodic.html', "r")

    # Reading the file and storing in a variable
contents = HTMLFileToBeOpened.read()
beautifulSoupText = BeautifulSoup(str(contents), 'html.parser')
data = beautifulSoupText.find_all('span', class_='nounderlines')


for d in data:
    data_Test.append(d.decode_contents())

for d in data_Test:
    data_Test2.append(BeautifulSoup(d,'html.parser').find_all('span'))

for i in range(len(data_Test2)):
    temp_arr={}
    for m in range(len(data_Test2[i])):
        if(i<=55):
            if(m==2):
                temp_arr["Z"]=int(periodic(data_Test2[i][m]))
            elif(m==3):
                temp_arr["SYMBOL"]=periodic(data_Test2[i][m])
            elif(m==5):
                temp_arr["AMU"]=float(periodic(data_Test2[i][m]))
            else:
                pass
        else:
            pass
    data_Test3[i+1]=temp_arr

data_Test4=[]
for i in range(len(data_Test2)):
    temp_arr={}
    if(i>55):
        if len(data_Test2[i])==7:
            for j in range(len(data_Test2[i])):
                temp_arr["Z"]=int(periodic(data_Test2[i][2]))
                temp_arr["SYMBOL"]=periodic(data_Test2[i][3])
                temp_arr["AMU"]=float(periodic(data_Test2[i][5]))
        elif len(data_Test2[i])==5:
            for j in range(len(data_Test2[i])):
                temp_arr["Z"]=int(periodic(data_Test2[i][2]))
                temp_arr["SYMBOL"]=periodic(data_Test2[i][3])
                list_to_Str = eval(str(periodic(data_Test2[i][4])).replace('\u200b',''))
                temp_arr["AMU"]=float(list_to_Str[0])
        data_Test4.append(temp_arr)
    else:
        pass
    
for key,val in data_Test3.items():
    for i in data_Test4:
        if(i["Z"]==int(key)):
            data_Test3[key]=i

#creating a Json file for Periodic Elements
with open("periodicTable.json", "w") as outfile:
    json.dump(data_Test3, outfile)

print("JSON FILE for Periodic Table Created")