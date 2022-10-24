from predict import _6numbersArray
import sys
import csv
import time

syms = ['\\', '|', '/', '-']
bs = '\b'
data = []
va = True
for _ in range(10):
    if (va == True):
        data = _6numbersArray
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

print("1st Digit: ", len(_1st_DigiPro))
print("2nd Digit: ", len(_2nd_DigiPro))
print("3rd Digit: ", len(_3rd_DigiPro))
print("4th Digit: ", len(_4th_DigiPro))
print("5th Digit: ", len(_5th_DigiPro))
print("6th Digit: ", len(_6th_DigiPro))
