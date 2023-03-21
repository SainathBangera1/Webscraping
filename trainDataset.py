import pandas as pd
import numpy as np
import csv

print("Following are the model names of csv file available")
print("1. 4PM_Combined.csv")
print("2. 5PM_Combined.csv")
print("3. 6PM_Combined.csv")
print("4. 7PM_Combined.csv")
print("5. 8PM_Combined.csv")

time = input("Enter the timeset of Data that you want from above options: ")

csvURL = time+'PM_Combined.csv'

data = pd.read_csv(csvURL)
data = np.array(data[["Day","Month","Year","Digit1","Digit2","Digit3","Digit4","Digit5","Digit6","Digit7","Digit8","Digit9","Digit10","Digit11","Digit12","Digit13","Digit14","Digit15","Digit16","Digit17","Digit18","Digit19","Digit20"]])

csvURL2 = time+'pmtrainDataset.csv'
with open(csvURL2,'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10'])
    for i in data:
        myFile.writerow(i)

print(f"{time}pmtrainDataset.csv completed . . . ")