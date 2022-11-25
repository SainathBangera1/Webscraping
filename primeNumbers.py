import random
import pandas as pd
import numpy as np
import csv
from dfunctions import duplicate, unionList, date_format, deltaDays, commanNumfromPairs, winPrimeNum,prime,date_Formater
import ast
from main import ball_1,ball_2,ball_3,ball_4,ball_5,ball_6

data = pd.read_csv('dataset.csv')
data = np.array(data[['Date','1st Digit','2nd Digit','3rd Digit','4th Digit','5th Digit','6th Digit']])

data_Output=[]
for i in range(len(data)):
    data[i][0] = date_Formater(data[i][0])
    tmp_arr=[data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6]]
    sum=0
    for x in range(1,7):
        tmp_arr.append(prime(data[i][x]))
        sum+=prime(data[i][x])
    tmp_arr.append(sum)
    sum=0
    data_Output.append(tmp_arr)

data_Title = ['Date','1st Digit','2nd Digit','3rd Digit','4th Digit','5th Digit','6th Digit','1st','2nd','3rd','4th','5th','6th','SUM']

with open('prime.csv','w') as file:
    myFile = csv.writer(file)
    myFile.writerow(data_Title)
    for i in data_Output:
        myFile.writerow(i)

print("Done writing prime.csv file...")

data_sum = pd.read_csv('prime.csv')
data_sum = np.array(data_sum[['Date','SUM']])

prim_count_arr=[]

for i in range(1,7):
    count=0
    for x in data_sum:
        if x[1]==i:
            count+=1
    prim_count_arr.append([i,count])
    count=0

# for i in prim_count_arr:
#     print(f"{i[0]} prime nums found {i[1]} out of {len(data)} draws {(i[1]/len(data))*100:.02f} %")

prime_num=[]
non_prime_num=[]

for i in range(1,91):
    if prime(i)==1:
        prime_num.append(i)
    else:
        non_prime_num.append(i)

# print(f"Prime nums: {prime_num} numbers ===> {len(prime_num)}")
# print(f"Non Prime nums: {non_prime_num} numbers ===> {len(non_prime_num)}")

first_Digit_Primes = list(set(ball_1) & set(prime_num))
first_Digit_NON_Primes=list(set(ball_1) - set(prime_num))
first_Digit_LEFT_Primes=list(set(prime_num) - set(first_Digit_Primes))

# num_1 = random.choice(first_Digit_NON_Primes)

# num_2 = random.choice(prime_num)

# num_3 = random.choice(prime_num)

# num_4 = random.choice(prime_num)

# num_5 = random.choice(non_prime_num)


# print(f"{first_Digit_Primes} length ===> {len(first_Digit_Primes)}")
# print(f"{first_Digit_LEFT_Primes} length ===> {len(first_Digit_LEFT_Primes)}")
# print(f"{first_Digit_NON_Primes} length ===> {len(first_Digit_NON_Primes)}")

sixth_Digit_Primes = list(set(ball_6) & set(prime_num))
sixth_Digit_NON_Primes=list(set(ball_6) - set(prime_num))
sixth_Digit_LEFT_Primes=list(set(prime_num) - set(sixth_Digit_Primes))

# num_6 = random.choice(sixth_Digit_NON_Primes)

# print(f"{sixth_Digit_Primes} length ===> {len(sixth_Digit_Primes)}")
# print(f"{sixth_Digit_LEFT_Primes} length ===> {len(sixth_Digit_LEFT_Primes)}")
# print(f"{sixth_Digit_NON_Primes} length ===> {len(sixth_Digit_NON_Primes)}")

print(f"Predicted Numbers: {winPrimeNum(first_Digit_NON_Primes,prime_num,prime_num,ball_4,ball_5,sixth_Digit_NON_Primes)}")
print("**********************************")
print(f"Predicted Numbers: {winPrimeNum(ball_1,ball_2,ball_3,ball_4,ball_5,ball_6)}")