from dataScrape import newDataSetArray
from datetime import datetime
import sys
import time
print("Loading....")
syms = ['\\', '|', '/', '-']
bs = '\b'

for _ in range(10):
    for sym in syms:
        sys.stdout.write("\b%s" % sym)
        sys.stdout.flush()
        time.sleep(0.5)
data = newDataSetArray
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
        if (i == data[j][6]):
            count += 1
    freq_6th_Digit.append([i, count])
    count = 0

print(freq_6th_Digit)
