import datetime
from datetime import datetime as dt
import ast
import random

weekdays = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]


def date_Day(dd, mm, yy):
    tday = datetime.date(yy, mm, dd)
    return weekdays[tday.isoweekday()]


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
