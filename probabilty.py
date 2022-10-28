from predict import _6numbersArray, freq_1st_Digit, freq_2nd_Digit, freq_3rd_Digit, freq_4th_Digit, freq_5th_Digit, freq_6th_Digit
from dataScrape import ascendingOrder
from dfunctions import deltaDays

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

# ******* TIME DELATS FOR Ball Number 1 in First Digit Column

ball_1_time_DELTA = []

for x in first_Digit_dates[0]:
    for y in range(len(first_Digit_dates[0][1])):
        if (y+1 < len(first_Digit_dates[0][1])):
            d1 = str(first_Digit_dates[0][1][y][2])+'/'+str(
                first_Digit_dates[0][1][y][1])+'/'+str(first_Digit_dates[0][1][y][0])
            d2 = str(first_Digit_dates[0][1][y+1][2])+'/'+str(
                first_Digit_dates[0][1][y+1][1])+'/'+str(first_Digit_dates[0][1][y+1][0])
            ball_1_time_DELTA.append(deltaDays(d2, d1))

print(ball_1_time_DELTA)

# print("2nd Digit: ", len(_2nd_DigiPro))
# print(_2nd_DigiPro)
# print("3rd Digit: ", len(_3rd_DigiPro))
# print(_3rd_DigiPro)
# print("4th Digit: ", len(_4th_DigiPro))
# print(_4th_DigiPro)
# print("5th Digit: ", len(_5th_DigiPro))
# print(_5th_DigiPro)
# print("6th Digit: ", len(_6th_DigiPro))
# print(_6th_DigiPro)

# Date, 1st_Prob, 2nd_Prob, 3rd_Prob, 4th_Prob, 5th_Prob, 6th_Prob
# prob_TITLE = ['Date', '1st', '2nd', '3rd', '4th', '5th', '6th', '1st_Prob', '2nd_Prob',
#               '3rd_Prob', '4th_Prob', '5th_Prob', '6th_Prob']
# prob_DATA = []

# for i in ascendingOrder:
#     temp_arr = []
#     temp_arr.append(i[1])
#     temp_arr.append(i[2])
#     temp_arr.append(i[3])
#     temp_arr.append(i[4])
#     temp_arr.append(i[5])
#     temp_arr.append(i[6])
#     temp_arr.append(i[7])
#     for a in range(len(freq_1st_Digit)):
#         if (freq_1st_Digit[a][0] == i[2]):
#             temp_arr.append(freq_1st_Digit[a][1])
#         if (freq_2nd_Digit[a][0] == i[3]):
#             temp_arr.append(freq_2nd_Digit[a][1])
#         if (freq_3rd_Digit[a][0] == i[4]):
#             temp_arr.append(freq_3rd_Digit[a][1])
#         if (freq_4th_Digit[a][0] == i[5]):
#             temp_arr.append(freq_4th_Digit[a][1])
#         if (freq_5th_Digit[a][0] == i[6]):
#             temp_arr.append(freq_5th_Digit[a][1])
#         if (freq_6th_Digit[a][0] == i[7]):
#             temp_arr.append(freq_6th_Digit[a][1])
#     prob_DATA.append(temp_arr)
#     temp_arr = []

# with open('dataProb.csv', 'w+') as file:
#     myFile = csv.writer(file)
#     myFile.writerow(prob_TITLE)
#     for i in range(len(prob_DATA)):
#         myFile.writerow([prob_DATA[i][0], prob_DATA[i][1], prob_DATA[i][2],
#                         prob_DATA[i][3], prob_DATA[i][4], prob_DATA[i][5], prob_DATA[i][6], prob_DATA[i][7], prob_DATA[i][8], prob_DATA[i][9], prob_DATA[i][10], prob_DATA[i][11], prob_DATA[i][12]])

# print("Done writing dataProb.csv ....")
