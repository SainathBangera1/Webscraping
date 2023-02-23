import pandas as pd
import numpy as np
import csv
import random
from dfunctions import dictFreq,odds,primes,sepratePrimes,seprateNonPrimes,duplicate,spitZero


#Magic DATA
dataONE = pd.read_csv('Magic.csv')
data1 = np.array(dataONE[['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5']])

digit_1 = np.array(dataONE['Digit1'])
digit_1 = spitZero(digit_1)
uni_dig_1 = list(set(digit_1)) # Length 20
freq_dig_1 = dictFreq(uni_dig_1,digit_1) # Even = 57% , Odd = 43%
#Prime = 41% , Non-Prime = 59%

digit_2 = np.array(dataONE['Digit2'])
digit_2 = spitZero(digit_2)
uni_dig_2 = list(set(digit_2)) # Length 24
freq_dig_2 = dictFreq(uni_dig_2,digit_2) # Even = 51% , Odd = 49%
# Prime = 65% , Non-Prime = 35%

digit_3 = np.array(dataONE['Digit3'])
digit_3 = spitZero(digit_3)
uni_dig_3 = list(set(digit_3)) # Length 26
freq_dig_3 = dictFreq(uni_dig_3,digit_3) # Even = 49% , Odd = 51%
#Prime = 72% , Non-Prime = 28%

digit_4 = np.array(dataONE['Digit4'])
digit_4 = spitZero(digit_4)
uni_dig_4 = list(set(digit_4)) # Length 33
freq_dig_4 = dictFreq(uni_dig_4,digit_4) # Even = 52% , Odd = 48%
#Prime = 75% , Non-Prime = 25%

digit_5 = np.array(dataONE['Digit5'])
digit_5 = spitZero(digit_5)
uni_dig_5 = list(set(digit_5)) # Length 35
freq_dig_5 = dictFreq(uni_dig_5,digit_5) # Even = 51% , Odd = 49%
#Prime = 78% , Non-Prime = 22%

#1st_SET ODD AND EVEN PERCENTAGE
firstSETArr = [odds(digit_1),odds(digit_2),odds(digit_3),odds(digit_4),odds(digit_5)]

# print("For First SET :")
# for i in firstSETArr:
#     print(f"Even = {i[0]}% , Odd = {i[1]}%")


#1st_SET PRIME and NON Prime Percentage
primeArr1 = [primes(digit_1),primes(digit_2),primes(digit_3),primes(digit_4),primes(digit_5)]

# print("Magic numbers :")
# for i in primeArr1:
#     print(f"Prime = {i[0]}% , Non-Prime = {i[1]}%")

digit_1_NonPRIME = list(set(seprateNonPrimes([],digit_1)))
digit_2_PRIME = list(set(sepratePrimes([],digit_2)))
digit_3_PRIME = list(set(sepratePrimes([],digit_3)))
digit_4_PRIME = list(set(sepratePrimes([],digit_4)))
digit_5_PRIME = list(set(sepratePrimes([],digit_5)))



num = [random.choice(digit_1_NonPRIME), random.choice(digit_2_PRIME), random.choice(digit_3_PRIME), random.choice(digit_4_PRIME),random.choice(digit_5_PRIME)]


dupli = duplicate(num)


while (len(dupli) > 0):
    for i in dupli:
        if (i == 0):
            num[i] = random.choice(digit_1_NonPRIME)
        elif (i == 1 ):
            num[i] = random.choice(digit_2_PRIME)
        elif (i == 2 ):
            num[i] = random.choice(digit_3_PRIME)
        elif (i == 3 ):
            num[i] = random.choice(digit_4_PRIME)
        elif (i == 4 ):
            num[i] = random.choice(digit_5_PRIME)
    dupli = duplicate(num)            

num.sort()

with open('magic_generated.csv','a+') as file:
    myFile = csv.writer(file)
    #myFile.writerow(["Digit_1","Digit_2","Digit_3","Digit_4","Digit_5","Digit_6","Digit_7","Digit_8","Digit_9","Digit_10"])
    myFile.writerow(num)
