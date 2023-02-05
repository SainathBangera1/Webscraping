import pandas as pd
import numpy as np
import csv


#FIRSTSET DATA
dataONE = pd.read_csv('8PM_FirstSET.csv')
data1 = np.array(dataONE[['Day','Month','Year','Digit1','Digit2','Digit3','Digit4','Digit5','Digit6','Digit7','Digit8','Digit9','Digit10']])

digit_1 = np.array(dataONE['Digit1'])
uni_dig_1 = list(set(digit_1)) # Length 20

digit_2 = np.array(dataONE['Digit2'])
uni_dig_2 = list(set(digit_2)) # Length 24

digit_3 = np.array(dataONE['Digit3'])
uni_dig_3 = list(set(digit_3)) # Length 26

digit_4 = np.array(dataONE['Digit4'])
uni_dig_4 = list(set(digit_4)) # Length 33

# digit_5 = np.array(dataONE['Digit5'])
# uni_dig_5 = list(set(digit_5)) # Length 35

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

digit2_4 = np.array(dataTWO['Digit4'])
uni_dig2_4 = list(set(digit2_4)) # Length 36

# digit2_5 = np.array(dataTWO['Digit5'])
# uni_dig2_5 = list(set(digit2_5)) # Length 36

digit2_6 = np.array(dataTWO['Digit6'])
uni_dig2_6 = list(set(digit2_6)) # Length 34

digit2_7 = np.array(dataTWO['Digit7'])
uni_dig2_7 = list(set(digit2_7)) # Length 31

digit2_8 = np.array(dataTWO['Digit8'])
uni_dig2_8 = list(set(digit2_8)) # Length 28

digit2_9 = np.array(dataTWO['Digit9'])
uni_dig2_9 = list(set(digit2_9)) # Length 23

digit2_10 = np.array(dataTWO['Digit10'])
uni_dig2_10 = list(set(digit2_10)) # Length 19




