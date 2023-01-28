import datetime
from datetime import datetime as dt
import ast
import random
from itertools import accumulate


weekdays = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]


def date_Day(dd, mm, yy):
    dd=int(dd)
    mm = int(mm)
    yy=int(yy)
    tday = datetime.date(yy, mm, dd)
    return weekdays[tday.isoweekday()]

# da='2022/12/10'.split('/')
# print(date_Day(da[2],da[1],da[0]))
#output = Saturday

def date_format(arr):
    res = str(arr[2])+'/'+str(arr[1])+'/'+str(arr[0])
    return res


def deltaDays(date1, date2):
    res = (dt.strptime(date1, "%Y/%m/%d") -
           dt.strptime(date2, "%Y/%m/%d")).days
    return res


def unionList(data1, data2):
    res = list(set(data1) | set(data2))
    return res


def dayCount(val, arr):
    count = 0
    for x in arr:
        if x == val:
            count += 1
    return count


def lisToDate(arr):
    res = str(arr[2])+'/'+str(arr[1])+'/'+str(arr[0])
    return res


def duplicate(test_list):
    oc_set = set()
    res = []
    for idx, val in enumerate(test_list):
        if val not in oc_set:
            oc_set.add(val)
        else:
            res.append(idx)
    return res


def pairUp(data):
    rg = len(data)
    res = []
    for m in data:
        inter = []
        for i in range(rg):
            tm_arr = list(set(m) & set(data[i]))
            if len(tm_arr) > 1:
                inter.append(tm_arr)
        res.append(inter)
    if (len(res) != 0):
        return res
    else:
        pass


# test = [[1, 2, 3, 4, 5, 6], [1, 3, 4, 5, 6, 7],
#         [0, 2, 3, 5, 88, 99], [5, 6, 2, 3, 77, 100], [66, 55, 2, 3, 77, 100]]
# res_arr = pairUp(test)

# for x in res_arr:
#     print(x)

# compare list helps to find the number paired numbers frequency by comparing big and small array


def compareList(arr1, arr2):
    count = 0
    freq = 0
    for i in arr1:
        count = (len(list(set(i) & set(arr2))))
        if (count == 6 and len(arr2) == 6):
            freq += 1
        elif (count == 5 and len(arr2) == 5):
            freq += 1
        elif (count == 4 and len(arr2) == 4):
            freq += 1
        elif (count == 3 and len(arr2) == 3):
            freq += 1
        elif (count == 2 and len(arr2) == 2):
            freq += 1
    return freq


# testArr = [[2, 3, 4, 5],
#            [2, 1, 4, 5], [2, 3, 4, 5], [1, 10, 3, 7]]
# testTarr = [2, 3, 4, 5]

# print(compareList(testArr, testTarr))
#output : 2


def pairTostring(arr):
    res = ''
    for i in arr:
        res += str(i)+'-'
    res = res[:-1]
    return res

# convert the string into Array


def strToarray(strr):
    res = []
    strin = strr.split('-')
    for i in strin:
        res.append(ast.literal_eval(i))
    return res


def checkPairInArr(ckArr, orgArr):
    count = 0
    dates = ''
    tm_arry = orgArr[1:]
    for m in tm_arry:
        count = (len(list(set(m) & set(ckArr))))
        if (count == 6 and len(ckArr) == 6):
            dates += date_format(ast.literal_eval(m[0]))+','
        elif (count == 5 and len(ckArr) == 5):
            dates += date_format(ast.literal_eval(m[0]))+','
        elif (count == 4 and len(ckArr) == 4):
            dates += date_format(ast.literal_eval(m[0]))+','
        elif (count == 3 and len(ckArr) == 3):
            dates += date_format(ast.literal_eval(m[0]))+','
        elif (count == 2 and len(ckArr) == 2):
            dates += date_format(ast.literal_eval(m[0]))+','
    dates = dates[:-1]
    return dates


# test = ['32-55-68-99-77', '32-55-68-99-78',
#         '32-56-68-99-77', '32-55-68-99-77', '32-55-68-99-77']
# test = list(set(test))
# res = []
# for x in test:
#     res.append(strToarray(x))

# print(res)

def commanNumfromPairs(arr):
    str_arry = ''
    for x in arr:
        if (x[1] > 15):
            str_arry += str(strToarray(x[0]))+','
    striNG = str_arry.replace(']', '')
    striNG = striNG.replace('[', '')
    striNG = '['+striNG+']'
    striNG = ast.literal_eval(striNG)
    res = list(set(striNG))
    return res


def winNUm(arr):
    numbers = [random.choice(arr), random.choice(arr), random.choice(
        arr), random.choice(arr), random.choice(arr), random.choice(arr)]

    dupli = duplicate(numbers)

    while (len(dupli) > 0):
        for i in dupli:
            if (i == 0):
                numbers[i] = random.choice(arr)
            elif (i == 1):
                numbers[i] = random.choice(arr)
            elif (i == 2):
                numbers[i] = random.choice(arr)
            elif (i == 3):
                numbers[i] = random.choice(arr)
            elif (i == 4):
                numbers[i] = random.choice(arr)
            elif (i == 5):
                numbers[i] = random.choice(arr)
        dupli = duplicate(numbers)
    return numbers
# test = [[[2, 3], 10], [[3, 4], 11], [[5, 6], 12], [[5, 6], 9], [[2, 3], 20]]

# print(commanNumfromPairs(test))

#checks whether the number is prime or not
def prime(num):
    for i in range(2,num):
        if num%i == 0:
            return 0
            break
    else:
        return 1

#Format String Date of dataset.csv
def date_Formater(str):
    str = str.replace(" ",'')
    str = str.split('/')
    str = str[2]+'/'+str[1]+'/'+str[0]
    return str

#WINUMBERS USING 
def winPrimeNum(arr1,arr2,arr3,arr4,arr5,arr6):
    numbers = [random.choice(arr1), random.choice(arr2), random.choice(
        arr3), random.choice(arr4), random.choice(arr5), random.choice(arr6)]

    dupli = duplicate(numbers)

    while (len(dupli) > 0):
        for i in dupli:
            if (i == 0):
                numbers[i] = random.choice(arr1)
            elif (i == 1):
                numbers[i] = random.choice(arr2)
            elif (i == 2):
                numbers[i] = random.choice(arr3)
            elif (i == 3):
                numbers[i] = random.choice(arr4)
            elif (i == 4):
                numbers[i] = random.choice(arr5)
            elif (i == 5):
                numbers[i] = random.choice(arr6)
        dupli = duplicate(numbers)
    return numbers

#Factorize the number if its not prime
def factors(num):
    strING=''
    if(prime(num)==0):
        for i in range(2,num):
            if num%i == 0:
                strING+=str(i)+' x '
        strING = strING[:-1]
        strING = strING[:-1]
        strING = strING[:-1]
        return strING
    else:
        return "Prime"

# print(factors(50))

#Finiding Difference between Two numbers
def sub(a,b):
    return a-b

def trials(arr,ball_1,ball_2,ball_3,ball_4,ball_5,ball_6):
    #TRIAL AND ERROR
    count=0
    get=1
    original_Number = arr

    while (get!=0):
        pred_Arr = winPrimeNum(ball_1,ball_2,ball_3,ball_4,ball_5,ball_6)
        pred_Arr.sort()
        if(str(pred_Arr) == str(original_Number)):
            return pred_Arr
            get=0
        else:
            count+=1
            return count

#converts Array into strings
def arr_str(arr):
    res = str(arr[0])+','+str(arr[1])+','+str(arr[2])+','+str(arr[3])+','+str(arr[4])+','+str(arr[5])
    return res
#input = [3,4,5,6]
#output = '3,4,5,6'

def factorizor(num):
    if(prime(num)==0):
        tmp_arr=[]
        for i in range(2,num):
            if num%i==0 and prime(i)==1:
                tmp_arr.append(i)
        return tmp_arr[len(tmp_arr)-1]

# num = int(input("Enter a number to check Prime or NOT: "))
# print(factorizor(num))
#input = 22575
#output = 43

def arr_string(arr):
    res = str(arr[0])+'-'+str(arr[1])+'-'+str(arr[2])+'-'+str(arr[3])+'-'+str(arr[4])+'-'+str(arr[5])
    return res

def spitODDEVEN(num):
    odd=[]
    even=[]
    res=[]
    for i in range(1,num+1):
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    res.append(odd)
    res.append(even)
    return res
# print(spitODDEVEN(45))
#input = 45
#output = [
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45], 
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
# ]

def spitPrime(num):
    res=[]
    prime=[]
    nonPrime=[]
    for i in range(1,num+1):
        if(prime(i)==0):
            nonPrime.append(i)
        else:
            prime.append(i)
    res.append(prime)
    res.append(nonPrime)
    return res

#extracting elements detail from periodic table of wikipedia
def periodic(data):
    da = str(data)
    da=da.replace('</span>','')
    da=da[::-1]
    res=''
    for i in range(len(da)):
        if(da[i]=='>'):
            break
        res+=da[i]
    res=res[::-1]
    return res

#sorting the letters within the strings
def sortString(str):
    return tuple(accumulate(sorted(str)))[-1]

# Python program to remove duplicate character
# from character array and print in sorted
# order
def removeDuplicate(str):
    s = set()
     
    # Create a set using String characters
    for i in str:
        s.add(i)
 
    # Print content of the set
    st = ""
    for i in s:
        st = st+i
    return st