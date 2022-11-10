from predict import _6numbersArray, freq_1st_Digit, freq_2nd_Digit, freq_3rd_Digit, freq_4th_Digit, freq_5th_Digit, freq_6th_Digit
from dataScrape import ascendingOrder
from dfunctions import deltaDays, unionList, dayCount, lisToDate, date_format
import math
import sys
import csv
import time

syms = ['\\', '|', '/', '-']
bs = '\b'
data = []
data_set = []
va = True
for _ in range(10):
    if (va == True):
        data = _6numbersArray
        data_set = ascendingOrder
        va = False
    for sym in syms:
        sys.stdout.write("\b%s" % sym)
        sys.stdout.flush()
        time.sleep(0.3)
print("Data Loading Completed..")

_1st_DigiPro = []
_2nd_DigiPro = []
_3rd_DigiPro = []
_4th_DigiPro = []
_5th_DigiPro = []
_6th_DigiPro = []

# _6numbersArray = [[1st-[a,b]],[2nd-[a,b]],[3rd-[a,b]],[4th-[a,b]],[5th-[a,b]],[6th-[a,b]]]

for i in range(0, 6):
    for x in _6numbersArray[i]:
        if (x[1] != 0 and i == 0):
            _1st_DigiPro.append(x[0])
        elif (x[1] != 0 and i == 1):
            _2nd_DigiPro.append(x[0])
        elif (x[1] != 0 and i == 2):
            _3rd_DigiPro.append(x[0])
        elif (x[1] != 0 and i == 3):
            _4th_DigiPro.append(x[0])
        elif (x[1] != 0 and i == 4):
            _5th_DigiPro.append(x[0])
        elif (x[1] != 0 and i == 5):
            _6th_DigiPro.append(x[0])

first_Digit_dates = []
second_Digit_dates = []
third_Digit_dates = []
fourth_Digit_dates = []
fifth_Digit_dates = []
sixth_Digit_dates = []

for x in _1st_DigiPro:
    temp_arr = []
    for y in data_set:
        if (y[2] == x):
            temp_arr.append(y[0])
    first_Digit_dates.append([x, temp_arr])
    temp_arr = []

for x in _2nd_DigiPro:
    temp_arr = []
    for y in data_set:
        if (y[2] == x):
            temp_arr.append(y[0])
    second_Digit_dates.append([x, temp_arr])
    temp_arr = []

for x in _3rd_DigiPro:
    temp_arr = []
    for y in data_set:
        if (y[2] == x):
            temp_arr.append(y[0])
    third_Digit_dates.append([x, temp_arr])
    temp_arr = []

for x in _4th_DigiPro:
    temp_arr = []
    for y in data_set:
        if (y[2] == x):
            temp_arr.append(y[0])
    fourth_Digit_dates.append([x, temp_arr])
    temp_arr = []

for x in _5th_DigiPro:
    temp_arr = []
    for y in data_set:
        if (y[2] == x):
            temp_arr.append(y[0])
    fifth_Digit_dates.append([x, temp_arr])
    temp_arr = []

for x in _6th_DigiPro:
    temp_arr = []
    for y in data_set:
        if (y[2] == x):
            temp_arr.append(y[0])
    sixth_Digit_dates.append([x, temp_arr])
    temp_arr = []

# print("1st Digit: ", len(_1st_DigiPro))
# print(_1st_DigiPro)
# for x in first_Digit_dates:
#     print(x)
# first_Digit_dates = [[Ball number 1, [Date1, Date2 , . . . . Date_N]] , [Ball number 2, [Date1, Date2 , . . . . Date_N]]]
# print(first_Digit_dates[0][0])
# print(str(first_Digit_dates[0][1][0][0])+' - '+str(first_Digit_dates[0]
#       [1][0][1])+' - '+str(first_Digit_dates[0][1][0][2]))
# output = 22 - 1 - 2009

# ******* TIME DELATS FOR First Digit Column

_time_DELTA = []

for x in range(len(first_Digit_dates)):
    temp_arr = []
    temp_arr.append(first_Digit_dates[x][0])
    for y in range(len(first_Digit_dates[x][1])):
        if (y+1 < len(first_Digit_dates[x][1])):
            d1 = lisToDate(first_Digit_dates[x][1][y])
            d2 = lisToDate(first_Digit_dates[x][1][y+1])
            temp_arr.append(deltaDays(d2, d1))
    _time_DELTA.append(temp_arr)

# FOR Ball number 1 Deltas
# delta_TITLE = ["Ball Num", "deltas"]
# with open('1st_Digit_deltas.csv', 'w+') as file:
#     myFile = csv.writer(file)
#     myFile.writerow(delta_TITLE)
#     for i in range(len(_time_DELTA[0])):
#         if (i+1 < len(_time_DELTA[0])):
#             myFile.writerow([_time_DELTA[0][0], _time_DELTA[0][i+1]])


# ******* 1st and 6th Digit INTERSECTION AND EXCLUSIONS***********

firstINTERSECTsixth = list(set(_1st_DigiPro) & set(_6th_DigiPro))

firstExcludingsixth = list(set(_1st_DigiPro) - set(_6th_DigiPro))

sixthExcludingfirst = list(set(_6th_DigiPro) - set(_1st_DigiPro))

first_6th = unionList(firstExcludingsixth, sixthExcludingfirst)
# ******* 2nd and 5th Digit INTERSECTION AND EXCLUSIONS***********

secondINTERSECTfifth = list(set(_2nd_DigiPro) & set(_5th_DigiPro))

secondExcludingfifth = list(set(_2nd_DigiPro) - set(_5th_DigiPro))

fifthExcludingsecond = list(set(_5th_DigiPro) - set(_2nd_DigiPro))

second_5th = unionList(secondExcludingfifth, fifthExcludingsecond)

# ******* 3rd and 4th Digit INTERSECTION AND EXCLUSIONS***********

thirdINTERSECTfourth = list(set(_3rd_DigiPro) & set(_4th_DigiPro))

thirdExcludingfourth = list(set(_3rd_DigiPro) - set(_4th_DigiPro))

fourthExcludingthird = list(set(_4th_DigiPro) - set(_3rd_DigiPro))

third_4th = unionList(thirdExcludingfourth, fourthExcludingthird)


# print(len(firstINTERSECTsixth))
# print('*************************')
# print(len(first_6th))


# print(first_Digit_dates[0])
temp_arr = []
for x in first_Digit_dates[0][1]:
    temp_arr.append(x[0])

unique_num1 = list(set(temp_arr))

freq_days_num1 = []
for x in unique_num1:
    count = dayCount(x, temp_arr)
    freq_days_num1.append([x, count])

temp_arr = []

for z in unique_num1:
    temp_set_arr = []
    temp_set_arr.append(z)
    for y in first_Digit_dates[0][1]:
        if (y[0] == z):
            temp_set_arr.append(lisToDate(y))
    temp_arr.append(temp_set_arr)
    temp_set_arr = []

new_temp = []

for z in unique_num1:
    temp_set_arr = []
    temp_set_arr.append(z)
    for y in range(len(temp_arr[z-1][1:])):
        if (y+1 < len(temp_arr[z-1][1:])):
            d1 = temp_arr[z-1][1:][y]
            d2 = temp_arr[z-1][1:][y+1]
            temp_set_arr.append(deltaDays(d2, d1))
    new_temp.append(temp_set_arr)
    temp_set_arr = []

# print(new_temp)

# FOR Days of Ball num 1 Deltas REPEATS
# delta_TITLE = ["Day", "Time_deltas"]
# with open('TIME_Digit_deltas.csv', 'w+') as file:
#     myFile = csv.writer(file)
#     myFile.writerow(delta_TITLE)
#     for i in new_temp:
#         myFile.writerow(i)

# Date, 1st_Prob, 2nd_Prob, 3rd_Prob, 4th_Prob, 5th_Prob, 6th_Prob
prob_TITLE = ['Date', '1st', '2nd', '3rd', '4th', '5th', '6th', '1st_Prob', '2nd_Prob',
              '3rd_Prob', '4th_Prob', '5th_Prob', '6th_Prob']
prob_DATA = []

for i in ascendingOrder:
    temp_arr = []
    temp_arr.append(i[1])
    temp_arr.append(i[2])
    temp_arr.append(i[3])
    temp_arr.append(i[4])
    temp_arr.append(i[5])
    temp_arr.append(i[6])
    temp_arr.append(i[7])
    for a in range(len(freq_1st_Digit)):
        if (freq_1st_Digit[a][0] == i[2]):
            temp_arr.append(freq_1st_Digit[a][1])
        if (freq_2nd_Digit[a][0] == i[3]):
            temp_arr.append(freq_2nd_Digit[a][1])
        if (freq_3rd_Digit[a][0] == i[4]):
            temp_arr.append(freq_3rd_Digit[a][1])
        if (freq_4th_Digit[a][0] == i[5]):
            temp_arr.append(freq_4th_Digit[a][1])
        if (freq_5th_Digit[a][0] == i[6]):
            temp_arr.append(freq_5th_Digit[a][1])
        if (freq_6th_Digit[a][0] == i[7]):
            temp_arr.append(freq_6th_Digit[a][1])
    prob_DATA.append(temp_arr)
    temp_arr = []

with open('dataProb.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(prob_TITLE)
    for i in range(len(prob_DATA)):
        myFile.writerow([prob_DATA[i][0], prob_DATA[i][1], prob_DATA[i][2],
                        prob_DATA[i][3], prob_DATA[i][4], prob_DATA[i][5], prob_DATA[i][6], prob_DATA[i][7], prob_DATA[i][8], prob_DATA[i][9], prob_DATA[i][10], prob_DATA[i][11], prob_DATA[i][12]])

print("Done writing dataProb.csv ....")

time_date_DELTAS = []
for i in range(1, 91):
    temp_arr = []
    # for x in ascendingOrder[:int(len(ascendingOrder) - math.floor(len(ascendingOrder)*0.20))]:
    for x in ascendingOrder:
        if i in x[2:8]:
            temp_arr.append(date_format(x[0]))
    temp_arr.insert(0, i)
    time_date_DELTAS.append(temp_arr)


time_DELTAS = []
for x in time_date_DELTAS:
    temp_list = x[1:]
    temp_arr = []
    for y in range(len(temp_list)):
        if (y+1 < len(temp_list)):
            temp_arr.append(deltaDays(temp_list[y+1], temp_list[y]))
    temp_arr.insert(0, x[0])
    time_DELTAS.append(temp_arr)

# max_vall helps to set the value of number of columns required for CSV
max_val = []
for y in time_DELTAS:
    max_val.append(len(y))

# create time deltas column based on max_value
# delta_TITLE= [Ball Number, 1st, 2nd, . . . . . .167th]
delta_TITLE = ["Ball Number"]
for i in range(1, max(max_val)+1):
    delta_TITLE.append(f"Point {i}")

with open('deltas.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(delta_TITLE)
    for i in time_DELTAS:
        myFile.writerow(i)

print("Created and modified deltas.csv file Ready to use...")

print("Program terminated..")
