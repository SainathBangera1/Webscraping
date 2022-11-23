import random
import pandas as pd
import numpy as np
import csv
from dfunctions import duplicate, unionList, date_format, deltaDays, commanNumfromPairs, winNUm
from pdClassifier import dataNew
import ast


ball_Array = []
for i in range(1, 91):
    ball_Array.append(i)

data = pd.read_csv('dataFreq.csv')

ball = np.array(data[['Ball Numbers', '1st Digit Freq',
                '2nd Digit Freq', '3rd Digit Freq', '4th Digit Freq', '5th Digit Freq', '6th Digit Freq']])

ball_1 = []
ball_2 = []
ball_3 = []
ball_4 = []
ball_5 = []
ball_6 = []

for i in ball:
    if (i[1] > 1):
        ball_1.append(i[0])
for i in ball:
    if (i[2] > 10):
        ball_2.append(i[0])
for i in ball:
    if (i[3] > 5):
        ball_3.append(i[0])
for i in ball:
    if (i[4] > 5):
        ball_4.append(i[0])
for i in ball:
    if (i[5] > 10):
        ball_5.append(i[0])
for i in ball:
    if (i[6] > 1):
        ball_6.append(i[0])

ball_1_New = list(set(ball_1) & set(ball_6))
ball_1Exc6 = list(set(ball_1) - set(ball_6))
ball_6Exc1 = list(set(ball_6) - set(ball_1))
ball_6_New = unionList(ball_1Exc6, ball_6Exc1)
#print(f'Ball 1 and 6 : {len(ball_1_New)} ,  {len(ball_6_New)}')

ball_2_New = list(set(ball_2) & set(ball_5))
ball_2Exc5 = list(set(ball_2) - set(ball_5))
ball_5Exc2 = list(set(ball_5) - set(ball_2))
ball_5_New = unionList(ball_2Exc5, ball_5Exc2)

# print(f'Ball 2 and 5 : {len(ball_2_New)} ,  {len(ball_5_New)}')


ball_3_New = list(set(ball_3) & set(ball_4))
ball_3Exc4 = list(set(ball_3) - set(ball_4))
ball_4Exc3 = list(set(ball_4) - set(ball_3))
ball_4_New = unionList(ball_3Exc4, ball_4Exc3)

# print(f'Ball 3 and 4 : {len(ball_3_New)} ,  {len(ball_4_New)}')

num = [random.choice(ball_1_New), random.choice(ball_2_New), random.choice(
    ball_4_New), random.choice(ball_3_New), random.choice(ball_5_New), random.choice(ball_6_New)]


dupli = duplicate(num)


while (len(dupli) > 0):
    for i in dupli:
        if (i == 0):
            num[i] = random.choice(ball_1_New)
        elif (i == 1):
            num[i] = random.choice(ball_2_New)
        elif (i == 2):
            num[i] = random.choice(ball_3_New)
        elif (i == 3):
            num[i] = random.choice(ball_4_New)
        elif (i == 4):
            num[i] = random.choice(ball_5_New)
        elif (i == 5):
            num[i] = random.choice(ball_6_New)
    dupli = duplicate(num)

# print(
#     f"Wining Numbers PRE: {num[0]}, {num[1]}, {num[2]},{num[3]}, {num[4]}, {num[5]}")

###################################################################################################################

# day = int(input("Please Enter the Day: "))
# month = int(input("Please Enter the Month: "))
# year = int(input("Please Enter the Year: "))

# input_DATE = [day, month, year]

# fu_date = date_format(input_DATE)

# pre_delta_nums = {}

# for y in range(len(dataNew)):
#     pre_delta_nums[str(dataNew[y][0])] = deltaDays(
#         fu_date, dataNew[y][1]) % dataNew[y][2]
# print(
#     f"Result of Ball no: {dataNew[y][0]} - {deltaDays(fu_date,dataNew[y][1])%dataNew[y][2]}")

# max_Delta = max(predict_deltas)
# min_Delta = min(predict_deltas)

# sorts the value ascending order
#sort_value = sorted(pre_delta_nums.items(), key=lambda x: x[1])

# 10th Nov 2022
# original_val = [10, 16, 18, 34, 39, 45]
# 8 - 11 - 7 - 1 - 10

# 8th Nov 2022
# original_val = [15, 31, 33, 44, 46, 73]
# 1 - 1 - 5 - 7 - 3

# 5th Nov 2022
# original_val = [11, 18, 41, 50, 63, 74]
# 7 - 0 - 3 - 8 - 8
# mean_values = []


delta_TITLE = ["Ball Number", "Deltas"]

# with open('5th_Nov_2022.csv', 'w+') as file:
#     myFile = csv.writer(file)
#     myFile.writerow(delta_TITLE)
#     for i in range(len(sort_value)):
#         myFile.writerow([sort_value[i][0], sort_value[i][1]])
# print("Completed writing 5th_Nov_2022.csv...")

########################################## DATA_CSV_ANALYSIS #############################
# big_data = pd.read_csv('dataset.csv')

# sc_big_data = np.array(big_data[["List_Date", '1st Digit', '2nd Digit',
#                        '3rd Digit', '4th Digit', '5th Digit', '6th Digit']])


# data_CSV_analysis = []
# for i in sc_big_data:
#     temp_arr = []
#     temp_arr.append(date_format(ast.literal_eval(i[0])))
#     temp_arr.append(int(i[1]))
#     temp_arr.append(int(i[2]))
#     temp_arr.append(int(i[3]))
#     temp_arr.append(int(i[4]))
#     temp_arr.append(int(i[5]))
#     temp_arr.append(int(i[6]))
#     original_val = [int(i[1]), int(i[2]), int(
#         i[3]), int(i[4]), int(i[5]), int(i[6])]
#     pre_delta_nums = {}
#     for y in range(len(dataNew)):
#         pre_delta_nums[str(dataNew[y][0])] = deltaDays(
#             date_format(ast.literal_eval(i[0])), dataNew[y][1]) % dataNew[y][2]
#     sort_value = sorted(pre_delta_nums.items(), key=lambda x: x[1])

#     for i in range(len(sort_value)):
#         for x in original_val:
#             if (str(x) == sort_value[i][0]):
#                 temp_arr.append(sort_value[i][1])

#     data_CSV_analysis.append(temp_arr)

# data_CSV_TITLES = ["Date of Draw", "1st_D", "2nd_D", "3rd_D", "4th_D", "5th_D",
#                    "6th_D", '1st_Del', '2nd_Del', '3rd_Del', '4th_Del', '5th_Del', '6th_Del']

# with open('data_CSV_Analysis.csv', 'w+') as file:
#     myFile = csv.writer(file)
#     myFile.writerow(data_CSV_TITLES)
#     for i in data_CSV_analysis:
#         myFile.writerow(i)
# print("Completed writing data_CSV_analysis.csv file...")
# ##################################################################################################

# for i in range(len(sort_value)):
#     for x in original_val:
#         if (str(x) == sort_value[i][0]):
#             mean_values.append(sort_value[i][1])

# print(mean_values)

# 1st Digit : first_Val = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41]
# 2nd Digit : second_Val = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,54]
# 3rd Digit :  third_Value = [11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67]
# 4th Digit : fourth_Value = [24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79]
# 5th Digit : fifth_Value = [32,34,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89]
# 6th Digit : sixth_Value =[50,51,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]


first_Val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41]
second_Val = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
              25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 54]
third_Value = [11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
               38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
fourth_Value = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
fifth_Value = [32, 34, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
               62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
sixth_Value = [50, 51, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
               70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]


wining_Nums = []

numbers = [random.choice(first_Val), random.choice(second_Val), random.choice(
    third_Value), random.choice(fourth_Value), random.choice(fifth_Value), random.choice(sixth_Value)]


dupli = duplicate(numbers)


while (len(dupli) > 0):
    for i in dupli:
        if (i == 0):
            numbers[i] = random.choice(first_Val)
        elif (i == 1):
            numbers[i] = random.choice(second_Val)
        elif (i == 2):
            numbers[i] = random.choice(third_Value)
        elif (i == 3):
            numbers[i] = random.choice(fourth_Value)
        elif (i == 4):
            numbers[i] = random.choice(fifth_Value)
        elif (i == 5):
            numbers[i] = random.choice(sixth_Value)
    dupli = duplicate(numbers)


for i in range(0, 6):
    wining_Nums.append(numbers[i])

# print("\n")
# print(
#     f"WINING NUMBERS based on Values : {wining_Nums[0]},{wining_Nums[1]},{wining_Nums[2]},{wining_Nums[3]},{wining_Nums[4]},{wining_Nums[5]}")

# Wining number 12th Nov 2022 : 4,26,47,62,69,1

data = pd.read_csv('pairs_CSV.csv')
data = np.array(data[["Pairs", "Frequency"]])

pairsNUMBERS = commanNumfromPairs(data)

# print(f"Pair Numbers Length {len(pairsNUMBERS)}")

pairsNUMBERS = winNUm(pairsNUMBERS)


for i in range(0, 6):
    pairsNUMBERS.append(numbers[i])

# print("\n")
# print(
#     f"WINING NUMBERS based of PairNums : {pairsNUMBERS[0]},{pairsNUMBERS[1]},{pairsNUMBERS[2]},{pairsNUMBERS[3]},{pairsNUMBERS[4]},{pairsNUMBERS[5]}")
