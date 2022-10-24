import csv
from dataScrape import ascendingOrder

wheather_DATA = []

with open('./Wheater/Rome_Weather_Data.csv', 'r') as read_obj:

    # Return a reader object which will
    # iterate over lines in the given csvfile
    csv_reader = csv.reader(read_obj)

    # convert string to list
    list_of_csv = list(csv_reader)

    wheather_DATA.append(list_of_csv)

for i in range(1, len(wheather_DATA[0])):
    wheather_DATA[0][i][0] = int(wheather_DATA[0][i][0])
    wheather_DATA[0][i][1] = int(wheather_DATA[0][i][1])
    wheather_DATA[0][i][2] = int(wheather_DATA[0][i][2])
    wheather_DATA[0][i][3] = float(wheather_DATA[0][i][3])
    wheather_DATA[0][i][4] = float(wheather_DATA[0][i][4])
    wheather_DATA[0][i][5] = float(wheather_DATA[0][i][5])
    wheather_DATA[0][i][6] = float(wheather_DATA[0][i][6])
    wheather_DATA[0][i][7] = float(wheather_DATA[0][i][7])
    wheather_DATA[0][i][8] = float(wheather_DATA[0][i][8])
    wheather_DATA[0][i][9] = float(wheather_DATA[0][i][9])
    wheather_DATA[0][i][10] = float(wheather_DATA[0][i][10])
    wheather_DATA[0][i].insert(0, str(wheather_DATA[0][i][0])+' / ' +
                               str(wheather_DATA[0][i][1])+' / '+str(wheather_DATA[0][i][2]))


newData = []

for j in wheather_DATA[0]:
    newData.append(j)

wheather_DATA = newData


wht_Data = []

for i in range(len(ascendingOrder)):
    for j in range(len(wheather_DATA)):
        if (ascendingOrder[i][1] == wheather_DATA[j][0]):
            wht_Data.append(wheather_DATA[j])

wheather_DATA = wht_Data
print("Wheather Data Loaded...")
