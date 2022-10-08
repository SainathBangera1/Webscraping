from dataScrape import newDataSetArray
import sys
import time
import csv
print("Loading....")
syms = ['\\', '|', '/', '-']
bs = '\b'
data = []
va = True
for _ in range(10):
    if (va == True):
        data = newDataSetArray
        va = False
    for sym in syms:
        sys.stdout.write("\b%s" % sym)
        sys.stdout.flush()
        time.sleep(0.3)
# 9.779591seconds loading time

# 1st Digit Frequency
freq_1st_Digit = []
count = 0

for i in range(1, 91):
    for j in range(len(data)):
        if (i == data[j][2]):
            count += 1
    freq_1st_Digit.append([i, count])
    count = 0

# 2nd Digit Frequency
freq_2nd_Digit = []
count = 0

for i in range(1, 91):
    for j in range(len(data)):
        if (i == data[j][3]):
            count += 1
    freq_2nd_Digit.append([i, count])
    count = 0

# 3rd Digit Frequency
freq_3rd_Digit = []
count = 0

for i in range(1, 91):
    for j in range(len(data)):
        if (i == data[j][4]):
            count += 1
    freq_3rd_Digit.append([i, count])
    count = 0


# 4th Digit Frequency
freq_4th_Digit = []
count = 0

for i in range(1, 91):
    for j in range(len(data)):
        if (i == data[j][5]):
            count += 1
    freq_4th_Digit.append([i, count])
    count = 0


# 5th Digit Frequency
freq_5th_Digit = []
count = 0

for i in range(1, 91):
    for j in range(len(data)):
        if (i == data[j][6]):
            count += 1
    freq_5th_Digit.append([i, count])
    count = 0


# 6th Digit Frequency
freq_6th_Digit = []
count = 0

for i in range(1, 91):
    for j in range(len(data)):
        if (i == data[j][7]):
            count += 1
    freq_6th_Digit.append([i, count])
    count = 0

_6numbersArray = [freq_1st_Digit, freq_2nd_Digit,
                  freq_3rd_Digit, freq_4th_Digit, freq_5th_Digit, freq_6th_Digit]

graph_Heading = ["Ball Numbers", "1st Digit Freq", "2nd Digit Freq",
                 "3rd Digit Freq", "4th Digit Freq", "5th Digit Freq", "6th Digit Freq"]

# with open('dataFreq.csv', 'w+') as file:
#     myFile = csv.writer(file)
#     myFile.writerow(graph_Heading)
#     for i in range(len(freq_1st_Digit)):
#         myFile.writerow([freq_1st_Digit[i][0], freq_1st_Digit[i][1], freq_2nd_Digit[i][1],
#                         freq_3rd_Digit[i][1], freq_4th_Digit[i][1], freq_5th_Digit[i][1], freq_6th_Digit[i][1]])

difference_Heading = ["Ball Numbers", "1st Digit - 6th Digit Freq", "2nd Digit - 5th Digit",
                      "3rd Digit - 4th Digit"]


difference_Array_1 = []
difference_Array_2 = []
difference_Array_3 = []
# data index = [0 , 1 , 2(1st) , 3(2nd) , 4(3rd) , 5(4th), 6(5th) , 7(6th), 8, 9]
# data = [[list_array date],str_date,1st, 2nd, 3rd, 4th, 5th, 6th,jolly, superstar]
for i in range(len(data)):
    difference_Array_1.append(abs(data[i][7] - data[i][2]))
    difference_Array_2.append(abs(data[i][4] - data[i][5]))
    difference_Array_3.append(abs(data[i][3] - data[i][6]))

difference_Array_1 = list(set(difference_Array_1))
difference_Array_2 = list(set(difference_Array_2))
difference_Array_3 = list(set(difference_Array_3))
# # for j in range(len(difference_Array_1)):
# #     print(difference_Array_1[j])

# print(str(set(difference_Array_1)))
# print(str(set(difference_Array_2)))
# print(str(set(difference_Array_3)))

date_Ball_Difference_1 = []

for i in range(len(difference_Array_1)):
    setComman = []
    for j in range(len(data)):
        if (difference_Array_1[i] == abs(data[j][7]-data[j][2])):
            setComman.append(data[j][1])
    if (setComman != []):
        setComman.insert(0, difference_Array_1[i])
        date_Ball_Difference_1.append(setComman)
    setComman = []


# with open('difference_1.csv', 'w+') as file:
#     myFile = csv.writer(file)
#     for i in date_Ball_Difference:
#         myFile.writerow(i)

difference_Array_1_REPEAT = []


for i in range(len(date_Ball_Difference_1)):
    difference_Array_1_REPEAT.append(
        [date_Ball_Difference_1[i][0], (len(date_Ball_Difference_1[i])-1)])

with open('difference_1_REPEAT.csv', 'w+') as file:
    myFile = csv.writer(file)
    for i in difference_Array_1_REPEAT:
        myFile.writerow(i)


date_Ball_Difference_2 = []

for i in range(len(difference_Array_2)):
    setComman = []
    for j in range(len(data)):
        if (difference_Array_2[i] == abs(data[j][7]-data[j][2])):
            setComman.append(data[j][1])
    if (setComman != []):
        setComman.insert(0, difference_Array_2[i])
        date_Ball_Difference_2.append(setComman)
    setComman = []


difference_Array_2_REPEAT = []


for i in range(len(date_Ball_Difference_2)):
    difference_Array_2_REPEAT.append(
        [date_Ball_Difference_2[i][0], (len(date_Ball_Difference_2[i])-1)])

with open('difference_2_REPEAT.csv', 'w+') as file:
    myFile = csv.writer(file)
    for i in difference_Array_2_REPEAT:
        myFile.writerow(i)


date_Ball_Difference_3 = []

for i in range(len(difference_Array_3)):
    setComman = []
    for j in range(len(data)):
        if (difference_Array_3[i] == abs(data[j][7]-data[j][2])):
            setComman.append(data[j][1])
    if (setComman != []):
        setComman.insert(0, difference_Array_3[i])
        date_Ball_Difference_3.append(setComman)
    setComman = []


difference_Array_3_REPEAT = []


for i in range(len(date_Ball_Difference_3)):
    difference_Array_3_REPEAT.append(
        [date_Ball_Difference_3[i][0], (len(date_Ball_Difference_3[i])-1)])

with open('difference_3_REPEAT.csv', 'w+') as file:
    myFile = csv.writer(file)
    for i in difference_Array_3_REPEAT:
        myFile.writerow(i)


print("Program Terminated...")
