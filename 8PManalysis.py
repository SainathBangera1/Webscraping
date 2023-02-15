import pandas as pd
import numpy as np
import csv
import random
from dfunctions import dictFreq,odds,primes,sepratePrimes,seprateNonPrimes,duplicate,spitZero


#FIRSTSET DATA
dataONE = pd.read_csv('8PM_FirstSET.csv')
data1 = np.array(dataONE[['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10']])

digit_1 = np.array(dataONE['Digit1'])
digit_1 = spitZero(digit_1)
uni_dig_1 = list(set(digit_1)) # Length 20
freq_dig_1 = dictFreq(uni_dig_1,digit_1) # Even = 57% , Odd = 43%
#Prime = 29% , Non-Prime = 71%

digit_2 = np.array(dataONE['Digit2'])
digit_2 = spitZero(digit_2)
uni_dig_2 = list(set(digit_2)) # Length 24
freq_dig_2 = dictFreq(uni_dig_2,digit_2) # Even = 51% , Odd = 49%
# Prime = 55% , Non-Prime = 45%

digit_3 = np.array(dataONE['Digit3'])
digit_3 = spitZero(digit_3)
uni_dig_3 = list(set(digit_3)) # Length 26
freq_dig_3 = dictFreq(uni_dig_3,digit_3) # Even = 49% , Odd = 51%
#Prime = 67% , Non-Prime = 33%

digit_4 = np.array(dataONE['Digit4'])
digit_4 = spitZero(digit_4)
uni_dig_4 = list(set(digit_4)) # Length 33
freq_dig_4 = dictFreq(uni_dig_4,digit_4) # Even = 52% , Odd = 48%
#Prime = 69% , Non-Prime = 31%

digit_5 = np.array(dataONE['Digit5'])
digit_5 = spitZero(digit_5)
uni_dig_5 = list(set(digit_5)) # Length 35
freq_dig_5 = dictFreq(uni_dig_5,digit_5) # Even = 51% , Odd = 49%
#Prime = 70% , Non-Prime = 30%

# digit_6 = np.array(dataONE['Digit6'])
# uni_dig_6 = list(set(digit_6)) # Length 39

# digit_7 = np.array(dataONE['Digit7'])
# uni_dig_7 = list(set(digit_7)) # Length 38

# digit_8 = np.array(dataONE['Digit8'])
# uni_dig_8 = list(set(digit_8)) # Length 39

# digit_9 = np.array(dataONE['Digit9'])
# uni_dig_9 = list(set(digit_9)) # Length 38

# digit_10 = np.array(dataONE['Digit9'])
# uni_dig_10 = list(set(digit_10)) # Length 38


#SECONDSET DATA
dataTWO = pd.read_csv('8PM_SecondSET.csv')
data2 = np.array(dataTWO[['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10']])

# digit2_1 = np.array(dataTWO['Digit1'])
# uni_dig2_1 = list(set(digit2_1)) # Length 37

# digit2_2 = np.array(dataTWO['Digit2'])
# uni_dig2_2 = list(set(digit2_2)) # Length 38

# digit2_3 = np.array(dataTWO['Digit3'])
# uni_dig2_3 = list(set(digit2_3)) # Length 39

# digit2_4 = np.array(dataTWO['Digit4'])
# uni_dig2_4 = list(set(digit2_4)) # Length 36
# freq_dig2_4 = dictFreq(uni_dig2_4,digit2_4)

# digit2_5 = np.array(dataTWO['Digit5'])
# uni_dig2_5 = list(set(digit2_5)) # Length 36

digit2_6 = np.array(dataTWO['Digit6'])
digit2_6 = spitZero(digit2_6)
uni_dig2_6 = list(set(digit2_6)) # Length 34
freq_dig2_6 = dictFreq(uni_dig2_6,digit2_6) # Even = 46% , Odd = 54%
# Prime = 73% , Non-Prime = 27%

digit2_7 = np.array(dataTWO['Digit7'])
digit2_7 = spitZero(digit2_7)
uni_dig2_7 = list(set(digit2_7)) # Length 31
freq_dig2_7 = dictFreq(uni_dig2_7,digit2_7) # Even = 54% , Odd = 46%
# Prime = 76% , Non-Prime = 24%

digit2_8 = np.array(dataTWO['Digit8'])
digit2_8 = spitZero(digit2_8)
uni_dig2_8 = list(set(digit2_8)) # Length 28
freq_dig2_8 = dictFreq(uni_dig2_8,digit2_8) # Even = 48% , Odd = 52%
# Prime = 79% , Non-Prime = 21%

digit2_9 = np.array(dataTWO['Digit9'])
digit2_9 = spitZero(digit2_9)
uni_dig2_9 = list(set(digit2_9)) # Length 23
freq_dig2_9 = dictFreq(uni_dig2_9,digit2_9) # Even = 52% , Odd = 48%
# Prime = 77% , Non-Prime = 23%

digit2_10 = np.array(dataTWO['Digit10'])
digit2_10 = spitZero(digit2_10)
uni_dig2_10 = list(set(digit2_10)) # Length 19
freq_dig2_10 = dictFreq(uni_dig2_10,digit2_10) # Even = 44% , Odd = 56%
# Prime = 71% , Non-Prime = 29%

#1st_SET ODD AND EVEN PERCENTAGE
firstSETArr = [odds(digit_1),odds(digit_2),odds(digit_3),odds(digit_4),odds(digit_5)]
#2nd_SET ODD AND EVEN PERCENTAGE
secondSETArr = [odds(digit2_6),odds(digit2_7),odds(digit2_8),odds(digit2_9),odds(digit2_10)]

# print("For First SET :")
# for i in firstSETArr:
#     print(f"Even = {i[0]}% , Odd = {i[1]}%")

# print("For Second SET :")
# for i in secondSETArr:
#     print(f"Even = {i[0]}% , Odd = {i[1]}%")

#1st_SET PRIME and NON Prime Percentage
primeArr1 = [primes(digit_1),primes(digit_2),primes(digit_3),primes(digit_4),primes(digit_5)]
#1st_SET PRIME and NON Prime Percentage
primeArr2 = [primes(digit2_6),primes(digit2_7),primes(digit2_8),primes(digit2_9),primes(digit2_10)]

# print("For First SET :")
# for i in primeArr1:
#     print(f"Prime = {i[0]}% , Non-Prime = {i[1]}%")

# print("For Second SET :")
# for i in primeArr2:
#     print(f"Prime = {i[0]}% , Non-Prime = {i[1]}%")

# FOR 2ND SET NUMBERS
digit2_6_PRIME = list(set(sepratePrimes([],digit2_6)))
digit2_7_PRIME = list(set(sepratePrimes([],digit2_7)))
digit2_8_PRIME = list(set(sepratePrimes([],digit2_8)))
digit2_9_PRIME = list(set(sepratePrimes([],digit2_9)))
digit2_10_PRIME = list(set(sepratePrimes([],digit2_10)))

#FOR 1ST SET NUMBERS
digit_5_PRIME = list(set(sepratePrimes([],digit_5)))
digit_4_PRIME = list(set(sepratePrimes([],digit_4)))

# print(digit2_6_PRIME)
# print(digit2_7_PRIME)
# print(digit2_8_PRIME)
# print(digit2_9_PRIME)
# print(digit2_10_PRIME)

prime_2nd_Sets = set(digit2_6_PRIME).union(digit2_7_PRIME)
prime_2nd_Sets = prime_2nd_Sets.union(set(digit2_8_PRIME))
prime_2nd_Sets = prime_2nd_Sets.union(set(digit2_9_PRIME))
prime_2nd_Sets = prime_2nd_Sets.union(set(digit2_10_PRIME))

# print(prime_2nd_Sets)


prime_1st_Sets = set(digit_4_PRIME).union(set(digit_5_PRIME))

# print(prime_1st_Sets)
# print(digit_5_PRIME)
# print(digit_4_PRIME)
digit_2_PRIME = list(set(seprateNonPrimes([],digit_2)))
digit_3_PRIME = list(set(seprateNonPrimes([],digit_3)))

# Number to choose from Prime Nos
primaryNums = list(prime_1st_Sets.union(prime_2nd_Sets))


# Non Primes
digit_1_PRIME = list(set(seprateNonPrimes([],digit_1)))

nonPrimaryNums = digit_1_PRIME

num = [random.choice(primaryNums), random.choice(primaryNums), random.choice(primaryNums), random.choice(primaryNums), random.choice(primaryNums), random.choice(primaryNums),random.choice(primaryNums),random.choice(nonPrimaryNums),random.choice(digit_2_PRIME),random.choice(digit_3_PRIME)]


dupli = duplicate(num)


while (len(dupli) > 0):
    for i in dupli:
        if (i == 0):
            num[i] = random.choice(primaryNums)
        elif (i == 1 ):
            num[i] = random.choice(primaryNums)
        elif (i == 2 ):
            num[i] = random.choice(primaryNums)
        elif (i == 3 ):
            num[i] = random.choice(primaryNums)
        elif (i == 4 ):
            num[i] = random.choice(primaryNums)
        elif (i == 5 ):
            num[i] = random.choice(primaryNums)
        elif (i == 6 ):
            num[i] = random.choice(primaryNums)
        elif (i == 7 ):
            num[i] = random.choice(nonPrimaryNums)
        elif (i == 8 ):
            num[i] = random.choice(digit_2_PRIME)
        elif (i == 9 ):
            num[i] = random.choice(digit_3_PRIME)
    dupli = duplicate(num)            

num.sort()

array_10_Results = []


for j in range(0,10):
    count=j
    tmp_num = [random.choice(primaryNums), random.choice(primaryNums), random.choice(primaryNums), random.choice(primaryNums), random.choice(primaryNums), random.choice(primaryNums),random.choice(primaryNums),random.choice(nonPrimaryNums),random.choice(digit_2_PRIME),random.choice(digit_3_PRIME)]

    dupli = duplicate(tmp_num)


    while (len(dupli) > 0):
        for i in dupli:
            if (i == 0):
                num[i] = random.choice(primaryNums)
            elif (i == 1 ):
                num[i] = random.choice(primaryNums)
            elif (i == 2 ):
                num[i] = random.choice(primaryNums)
            elif (i == 3 ):
                num[i] = random.choice(primaryNums)
            elif (i == 4 ):
                num[i] = random.choice(primaryNums)
            elif (i == 5 ):
                num[i] = random.choice(primaryNums)
            elif (i == 6 ):
                num[i] = random.choice(primaryNums)
            elif (i == 7 ):
                num[i] = random.choice(nonPrimaryNums)
            elif (i == 8 ):
                num[i] = random.choice(digit_2_PRIME)
            elif (i == 9 ):
                num[i] = random.choice(digit_3_PRIME)
        dupli = duplicate(tmp_num)            

    tmp_num.sort()

for i in array_10_Results:
    print(i)
# with open('generated.csv','a+') as file:
#     myFile = csv.writer(file)
#     #myFile.writerow(["Digit_1","Digit_2","Digit_3","Digit_4","Digit_5","Digit_6","Digit_7","Digit_8","Digit_9","Digit_10"])
#     myFile.writerow(num)