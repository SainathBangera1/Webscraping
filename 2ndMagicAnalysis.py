import pandas as pd
import numpy as np
import csv
import random
from dfunctions import dictFreq,odds,primes,sepratePrimes,seprateNonPrimes,duplicate,spitZero,generateNum


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
store_10_tickets=[]


num = generateNum(digit_1,digit_2,digit_3,digit_4,digit_5)

for i in range(100):
    num = generateNum(digit_1,digit_2,digit_3,digit_4,digit_5)
    store_10_tickets.append(num)

with open('magic2_generated.csv','a+') as file:
    myFile = csv.writer(file)
    for i in store_10_tickets:
        myFile.writerow(i)

print("10 tickets Generated in magic2_generated.csv")