import pandas as pd
import numpy as np
import csv
import random
from dfunctions import dictFreq,odds,primes,sepratePrimes,seprateNonPrimes,duplicate


#FIRSTSET DATA
dataONE = pd.read_csv('8PM_FirstSET.csv')
data1 = np.array(dataONE[['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10']])

digit_1 = np.array(dataONE['Digit1'])
uni_dig_1 = list(set(digit_1)) # Length 20
freq_dig_1 = dictFreq(uni_dig_1,digit_1) # Even = 57% , Odd = 43%
#Prime = 28% , Non-Prime = 72%

digit_2 = np.array(dataONE['Digit2'])
uni_dig_2 = list(set(digit_2)) # Length 24
freq_dig_2 = dictFreq(uni_dig_2,digit_2) # Even = 51% , Odd = 49%
# Prime = 56% , Non-Prime = 44%

digit_3 = np.array(dataONE['Digit3'])
uni_dig_3 = list(set(digit_3)) # Length 26
freq_dig_3 = dictFreq(uni_dig_3,digit_3) # Even = 49% , Odd = 51%
#Prime = 67% , Non-Prime = 33%

digit_4 = np.array(dataONE['Digit4'])
uni_dig_4 = list(set(digit_4)) # Length 33
freq_dig_4 = dictFreq(uni_dig_4,digit_4) # Even = 52% , Odd = 48%
#Prime = 68% , Non-Prime = 32%

digit_5 = np.array(dataONE['Digit5'])
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
uni_dig2_6 = list(set(digit2_6)) # Length 34
freq_dig2_6 = dictFreq(uni_dig2_6,digit2_6) # Even = 46% , Odd = 54%
# Prime = 77% , Non-Prime = 23%

digit2_7 = np.array(dataTWO['Digit7'])
uni_dig2_7 = list(set(digit2_7)) # Length 31
freq_dig2_7 = dictFreq(uni_dig2_7,digit2_7) # Even = 54% , Odd = 46%
# Prime = 77% , Non-Prime = 23%

digit2_8 = np.array(dataTWO['Digit8'])
uni_dig2_8 = list(set(digit2_8)) # Length 28
freq_dig2_8 = dictFreq(uni_dig2_8,digit2_8) # Even = 48% , Odd = 52%
# Prime = 74% , Non-Prime = 26%

digit2_9 = np.array(dataTWO['Digit9'])
uni_dig2_9 = list(set(digit2_9)) # Length 23
freq_dig2_9 = dictFreq(uni_dig2_9,digit2_9) # Even = 52% , Odd = 48%
# Prime = 78% , Non-Prime = 22%

digit2_10 = np.array(dataTWO['Digit10'])
uni_dig2_10 = list(set(digit2_10)) # Length 19
freq_dig2_10 = dictFreq(uni_dig2_10,digit2_10) # Even = 44% , Odd = 56%
# Prime = 75% , Non-Prime = 25%

num = [random.choice(uni_dig_1), random.choice(uni_dig_2), random.choice(uni_dig_3), random.choice(uni_dig_4), random.choice(uni_dig_5), random.choice(uni_dig2_6),random.choice(uni_dig2_7),random.choice(uni_dig2_8),random.choice(uni_dig2_9),random.choice(uni_dig2_10)]

dupli = duplicate(num)


while (len(dupli) > 0):
    for i in dupli:
        if (i == 0):
            num[i] = random.choice(uni_dig_1)
        elif (i == 1):
            num[i] = random.choice(uni_dig_2)
        elif (i == 2):
            num[i] = random.choice(uni_dig_3)
        elif (i == 3):
            num[i] = random.choice(uni_dig_3)
        elif (i == 4):
            num[i] = random.choice(uni_dig_4)
        elif (i == 5):
            num[i] = random.choice(uni_dig_5)
        elif (i == 6):
            num[i] = random.choice(uni_dig2_6)
        elif (i == 7):
            num[i] = random.choice(uni_dig2_7)
        elif (i == 8):
            num[i] = random.choice(uni_dig2_8)
        elif (i == 9):
            num[i] = random.choice(uni_dig2_9)
        elif (i==10):
            num[i] = random.choice(uni_dig2_10)
    dupli = duplicate(num)

num.sort()


with open('2generated.csv','a+') as file:
    myFile = csv.writer(file)
    #myFile.writerow(["Digit_1","Digit_2","Digit_3","Digit_4","Digit_5","Digit_6","Digit_7","Digit_8","Digit_9","Digit_10"])
    myFile.writerow(num)