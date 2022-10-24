from predict import data_for_Linear_Regression as data
import csv
data_1st_Digit = []
data_2nd_Digit = []
data_3rd_Digit = []
data_4th_Digit = []
data_5th_Digit = []
data_6th_Digit = []

for i in range(len(data)):
    date = str(data[i][3])+'-'+str(data[i][2])+'-'+str(data[i][1])
    data_1st_Digit.append([date, data[i][1], data[i][2],
                          data[i][3], data[i][4], data[i][4] % 2 == 0 and "Even" or "Odd", data[i][13], data[i][14], data[i][15], data[i][16], data[i][17], data[i][18], data[i][19], data[i][20]])
    data_2nd_Digit.append([date, data[i][1], data[i][2],
                          data[i][3], data[i][4], data[i][5] % 2 == 0 and "Even" or "Odd", data[i][13], data[i][14], data[i][15], data[i][16], data[i][17], data[i][18], data[i][19], data[i][20]])
    data_3rd_Digit.append([date, data[i][1], data[i][2],
                          data[i][3], data[i][4], data[i][6] % 2 == 0 and "Even" or "Odd", data[i][13], data[i][14], data[i][15], data[i][16], data[i][17], data[i][18], data[i][19], data[i][20]])
    data_4th_Digit.append([date, data[i][1], data[i][2],
                          data[i][3], data[i][4], data[i][7] % 2 == 0 and "Even" or "Odd", data[i][13], data[i][14], data[i][15], data[i][16], data[i][17], data[i][18], data[i][19], data[i][20]])
    data_5th_Digit.append([date, data[i][1], data[i][2],
                          data[i][3], data[i][4], data[i][8] % 2 == 0 and "Even" or "Odd", data[i][13], data[i][14], data[i][15], data[i][16], data[i][17], data[i][18], data[i][19], data[i][20]])
    data_6th_Digit.append([date, data[i][1], data[i][2],
                          data[i][3], data[i][4], data[i][9] % 2 == 0 and "Even" or "Odd", data[i][13], data[i][14], data[i][15], data[i][16], data[i][17], data[i][18], data[i][19], data[i][20]])


data_TOTAL = [data_1st_Digit, data_2nd_Digit, data_3rd_Digit,
              data_4th_Digit, data_5th_Digit, data_6th_Digit]
data_TOTAL_TITLE = ['data_1st_Digit', 'data_2nd_Digit', 'data_3rd_Digit',
                    'data_4th_Digit', 'data_5th_Digit', 'data_6th_Digit']
data_Title = ['Date', 'Day', 'Month', 'Year', '', 'OE', 'T2M', 'T2MDEW',
              'T2MWET', 'TS', 'T2M_RANGE', 'T2M_MAX', 'T2M_MIN', 'PRECTOTCORR']

for x in range(len(data_TOTAL)):
    with open(data_TOTAL_TITLE[x]+'.csv', 'w+') as file:
        myFile = csv.writer(file)
        data_Title[4] = data_TOTAL_TITLE[x]
        myFile.writerow(data_Title)
        for i in data_TOTAL[x]:
            myFile.writerow(i)
