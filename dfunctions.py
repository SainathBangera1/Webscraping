import datetime
from datetime import datetime as dt
import ast
import random
from itertools import accumulate
import numpy as np



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

def dictFreq(uni,arr):
    count=0
    tmp=[]
    for i in uni:
        for j in arr:
            if(i==j):
                count+=1
        tmp.append([i,count])
        count=0
    return tmp
    
#input = [2,3,5]
#input 2 = [2,3,3,6,7,8,9,2,2,2,7,7,8,5,5]
# print(dictFreq([2,3,5],[2,3,3,6,7,8,9,2,2,2,7,7,8,5,5]))
#output = [{2: 4}, {3: 2}, {5: 2}]

def odds(arr):
    countOdd=0
    countEven=0
    for i in arr:
        if (i%2==0):
            countEven+=1
        else:
            countOdd+=1
    resEven = round(((len(arr)-countEven)/len(arr))*100)
    resOdd = round(((len(arr)-countOdd)/len(arr))*100)
    return [resEven,resOdd]

def primes(arr):
    primes=0
    nonPrimes=0
    for i in arr:
        if (prime(i)==0):
            nonPrimes+=1
        else:
            primes+=1
    resPrime = round(((primes)/len(arr))*100)
    resNonPrime = round(((nonPrimes)/len(arr))*100)
    return [resPrime,resNonPrime]

# result = primes([1,9,11,16,20,32,34,35,36,37,39,40,45,47,50,63,74,77,78,79])
# print(f"Primes : {result[0]} %")
# print(f"Non Primes : {result[1]} %")

def sepratePrimes(store,data):
    for i in data:
        if(prime(i)==1):
            store.append(i)
    return store

def seprateNonPrimes(store,data):
    for i in data:
        if(prime(i)==0):
            store.append(i)
    return store


#inputArr = [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,19,20,21]
#comArr = [4,11,16,23,24,37,41,43,47,79]
#output = 3
def matchNum(inputArr,compArr):
    count=0
    for i in inputArr:
        for j in compArr:
            if(i==j):
                count+=1
    return count
# inputArr = [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,19,20,21]
# comArr = [4,11,16,23,24,37,41,43,47,79]
# print(matchNum(inputArr,comArr))

def spitZero(arr):
    tmp=[]
    for i in arr:
        if(i!=0):
            tmp.append(i)
    return tmp

def generateNum(ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10):
    num = [random.choice(ar1),random.choice(ar2),random.choice(ar3),random.choice(ar4),random.choice(ar5),random.choice(ar6),random.choice(ar7),random.choice(ar8),random.choice(ar9),random.choice(ar10)]
    dupli = duplicate(num)
    while (len(dupli) > 0):
        for i in dupli:
            if (i == 0):
                num[i] = random.choice(ar1)
            elif (i == 1 ):
                num[i] = random.choice(ar2)
            elif (i == 2 ):
                num[i] = random.choice(ar3)
            elif (i == 3 ):
                num[i] = random.choice(ar4)
            elif (i == 4 ):
                num[i] = random.choice(ar5)
            elif (i == 5 ):
                num[i] = random.choice(ar6)
            elif (i == 6 ):
                num[i] = random.choice(ar7)
            elif (i == 7 ):
                num[i] = random.choice(ar8)
            elif (i == 8 ):
                num[i] = random.choice(ar9)
            elif (i == 9 ):
                num[i] = random.choice(ar10)
        dupli = duplicate(num)            
    # num.sort() 
    return num

def compareList(arr1,arr2):
    tmp=list(set(arr1) & set(arr2))
    if(len(tmp)>0):
        return 1
    else:
        return 0

# a1 = [7,8,9]
# a2 = [3,5,7,8,9]

# print(compareList(a1,a2))


def delElements(ar1,ar2,ogData):
    for i in ar1:
        if(len(ar2)<6):
            ar2 = np.copy(ogData)
        if(i in ar2):
            ar2=np.delete(ar2, np.where(ar2 == i))
    return ar2


# def delElements1(ar1,ar2,ogData):
#     for i in ar1:
#         if(len(ar2)==1):
#             ar2 = np.copy(ogData)
#         if(i in ar2):
#             ar2=np.delete(ar2, np.where(ar2 == i))
#     return ar2


def generateMODEL1(arr):
    num = [random.choice(arr[:29]),random.choice(arr[:29]),random.choice(arr[:29]),random.choice(arr[:29]),random.choice(arr[:29]),random.choice(arr[29:]),random.choice(arr[29:]),random.choice(arr[29:]),random.choice(arr[29:]),random.choice(arr[29:])]
    dupli = duplicate(num)
    while (len(dupli) > 0):
        for i in dupli:
            if (i == 0):
                num[i] = random.choice(arr[:29])
            elif (i == 1 ):
                num[i] = random.choice(arr[:29])
            elif (i == 2 ):
                num[i] = random.choice(arr[:29])
            elif (i == 3 ):
                num[i] = random.choice(arr[:29])
            elif (i == 4 ):
                num[i] = random.choice(arr[:29])
            elif (i == 5 ):
                num[i] = random.choice(arr[29:])
            elif (i == 6 ):
                num[i] = random.choice(arr[29:])
            elif (i == 7 ):
                num[i] = random.choice(arr[29:])
            elif (i == 8 ):
                num[i] = random.choice(arr[29:])
            elif (i == 9 ):
                num[i] = random.choice(arr[29:])
        dupli = duplicate(num)            
    num.sort()
        
    return num


def generateMODEL2(arr):
    num = [random.choice(arr),random.choice(arr),random.choice(arr),random.choice(arr),random.choice(arr),random.choice(arr),random.choice(arr),random.choice(arr),random.choice(arr),random.choice(arr)]
    dupli = duplicate(num)
    while (len(dupli) > 0):
        for i in dupli:
            if (i == 0):
                num[i] = random.choice(arr)
            elif (i == 1 ):
                num[i] = random.choice(arr)
            elif (i == 2 ):
                num[i] = random.choice(arr)
            elif (i == 3 ):
                num[i] = random.choice(arr)
            elif (i == 4 ):
                num[i] = random.choice(arr)
            elif (i == 5 ):
                num[i] = random.choice(arr)
            elif (i == 6 ):
                num[i] = random.choice(arr)
            elif (i == 7 ):
                num[i] = random.choice(arr)
            elif (i == 8 ):
                num[i] = random.choice(arr)
            elif (i == 9 ):
                num[i] = random.choice(arr)
        dupli = duplicate(num)            
    num.sort()
        
    return num


def frequency(num,arr):
    count=0
    for i in arr:
        if(num==i):
            count+=1
    return count


def grt50Nprime(arr):
    ct50=0
    for i in arr:
        if(prime(i)==0 and i<50):
            ct50+=1
    return ct50


def next_number(arr):
    """
    Takes an array of non-sequential numbers and returns the next possible number in the sequence.
    """
    # Sort the array in ascending order
    arr = sorted(arr)
    
    # Find the difference between each adjacent pair of numbers in the array
    diffs = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    
    # Find the index of the first difference that is not 1
    idx = next((i for i, x in enumerate(diffs) if x != 1), None)
    
    # If all differences are 1, return the last element of the array plus 1
    if idx is None:
        return arr[-1] + 1
    
    # Otherwise, return the number that comes after the last number in the first sequential block
    else:
        return arr[idx] + 1

def checkit(stored,newNum):
    for i in stored:
        for j in i:
            if (j in newNum):
                return True    

def superenaNum(ar1,ar2,ar3,ar4,ar5,ar6):
    num = [random.choice(ar1),random.choice(ar2),random.choice(ar3),random.choice(ar4),random.choice(ar5),random.choice(ar6)]
    dupli = duplicate(num)
    while (len(dupli) > 0):
        for i in dupli:
            if (i == 0):
                num[i] = random.choice(ar1)
            elif (i == 1 ):
                num[i] = random.choice(ar2)
            elif (i == 2 ):
                num[i] = random.choice(ar3)
            elif (i == 3 ):
                num[i] = random.choice(ar4)
            elif (i == 4 ):
                num[i] = random.choice(ar5)
            elif (i == 5 ):
                num[i] = random.choice(ar6)
        dupli = duplicate(num)            
    # num.sort() 
    return num


def verticalFreq(arr1,arr2):
    for i in arr1:
        for j in arr2:
            if(i[0]==j[0]):
                j.append(i[1])
    return arr2

                    
def date_to_Timestamp(dateTime):
    # current date and time
    datetime_str = dateTime

    datetime_object = dt.strptime(datetime_str, '%d/%m/%y %H:%M:%S')

    timestamp = dt.timestamp(datetime_object)

    return timestamp

#timestamp = int(date_to_Timestamp('07/01/09 20:00:00'))

# def findSeed(timestp,target):
#     seed=timestp

#     while (True):
        
#         np.random.seed(seed)
        
#         nums = np.random.randint(1,91,size=6)
#         nums.sort()
#         if(len(list(set(target)-set(nums)))==0):
#             return seed
#         else:
#             pass
#         seed+=1

#print(findSeed(timestamp,[25,28,36,45,48,86]))
# diff = timestamp
# print(diff)
# np.random.seed(diff)
# nums = np.random.randint(1,91,size=6)
# print(nums)

def findSeed(timestp,target_Arr):
    tmp_arr=[]
    for i in range(len(target_Arr)):
        target=target_Arr[i]
        seed=timestp
        while (True):
            np.random.seed(seed)
            num=0
            if(i==0):
                num = np.random.randint(1,66)
            if(i==1):
                num = np.random.randint(2,83)
            if(i==2):
                num = np.random.randint(4,86)
            if(i==3):
                num = np.random.randint(9,88)
            if(i==4):
                num = np.random.randint(14,90)
            if(i==5):
                num = np.random.randint(26,91)
            if(i==6):
                num = np.random.randint(1,91)
            if(i==7):
                num = np.random.randint(1,91)
            if(num==target):
                tmp_arr.append(seed)
                break
            else:
                pass
            seed+=1
    return tmp_arr

#print(findSeed(timestamp,[25,28,36,45,48,86]))

# diff = findSeed(timestamp,[14,31,35,40,50,66])

# newNums=[]
# for i in diff:
#     np.random.seed(i)
#     num = np.random.randint(1,91)
#     newNums.append(num)
# print(diff)
# print(newNums)

def giveSEED(timestamp,target_Arr,realNum,index):
    for i in target_Arr:
        seedlings = timestamp+i
        num=0
        np.random.seed(seedlings)
        if(index==0):
            num=np.random.randint(1,66)
        if(index==1):
            num=np.random.randint(2,83)
        if(index==2):
            num=np.random.randint(4,86)
        if(index==3):
            num=np.random.randint(9,88)
        if(index==4):
            num=np.random.randint(14,90)
        if(index==5):
            num=np.random.randint(26,91)
        if(index==6):
            num=np.random.randint(1,91)
        if(index==7):
            num=np.random.randint(1,91)
        if(num==realNum[index]):
            return seedlings
    
# def seedDELTA(timestamp,target_Arr,index,minNum,maxNum,realNum):
#     for i in target_Arr[index]:
#         seedling=timestamp+i
#         np.random.seed(seedling)
#         num=np.random.randint(minNum,maxNum+1)
#         if(realNum[index]==num):
#             return seedling

def generateMODELTimestamp(arr):
    num = [random.choice(arr[0]),random.choice(arr[1]),random.choice(arr[2]),random.choice(arr[3]),random.choice(arr[4]),random.choice(arr[5])]
    dupli = duplicate(num)
    while (len(dupli) > 0):
        for i in dupli:
            if (i == 0):
                num[i] = random.choice(arr[0])
            elif (i == 1 ):
                num[i] = random.choice(arr[1])
            elif (i == 2 ):
                num[i] = random.choice(arr[2])
            elif (i == 3 ):
                num[i] = random.choice(arr[3])
            elif (i == 4 ):
                num[i] = random.choice(arr[4])
            elif (i == 5 ):
                num[i] = random.choice(arr[5])
            elif (i == 6 ):
                num[i] = random.choice(arr[6])
            elif (i == 7 ):
                num[i] = random.choice(arr[7])
        dupli = duplicate(num)            
        
    return num


def genNUMtimestamp(timestamp,arr):
    tmp_num_arr=generateMODELTimestamp(arr)
    timestamp_arr = []
    for i in tmp_num_arr:
        tm=timestamp+i
        timestamp_arr.append(tm)
    return timestamp_arr           

def getNumfromSEED(seedling,index):
    np.random.seed(seedling)
    num=0
    if(index==0):
            num=np.random.randint(1,66)
            return num
    if(index==1):
            num=np.random.randint(2,83)
            return num
    if(index==2):
            num=np.random.randint(4,86)
            return num
    if(index==3):
            num=np.random.randint(9,88)
            return num
    if(index==4):
            num=np.random.randint(14,90)
            return num
    if(index==5):
            num=np.random.randint(26,91)
            return num
    if(index==6):
            num=np.random.randint(1,91)
            return num
    if(index==7):
            num=np.random.randint(1,91)
            return num

#Recurssion function for Arithematic progression
def reApfunction(arr,val):
    count=val
    newArr=[]
    for i in range(len(arr)):
        if(i+1<len(arr)):
            newArr.append(arr[i+1]-arr[i])
    if(len(list(set(newArr)))==1):
        print(newArr)
        return count
    print(newArr)
    return reApfunction(newArr,count+1)
#input = [2,4,6,8,10,12,14]
# print(reApfunction(tmp_data,1))