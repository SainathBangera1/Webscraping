import datetime
from datetime import datetime as dt

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


def pairUp(data, i):
    pair1 = []

    pair_New = []
    for x in range(len(data)):
        temp_arr = []
        if (x+1 < len(data)):
            pair = set(data[i]) & set(data[x+1])
            if (len(list(pair)) > 1):
                temp_arr.append(pair)
        if (len(temp_arr) != 0):
            pair1.append(temp_arr)
        temp_arr = []

    for y in pair1:
        if (len(list(y[0])) > 2):
            pair_New.append(list(y[0]))

    return pair_New


# compare list helps to find the number paired numbers frequency by comparing big and small array
def compareList(arr1, arr2):
    count = 0
    freq = 0
    if (len(arr1) > len(arr2)):
        for i in range(len(arr1)):
            for m in arr2:
                if (m in arr1[i]):
                    count += 1
                if (count >= 3):
                    freq += 1
                    count = 0
    elif (len(arr2) > len(arr1)):
        for i in range(len(arr2)):
            for m in arr1:
                if (m in arr2[i]):
                    count += 1
                if (count >= 3):
                    freq += 1
                    count = 0
    return freq


def pairTostring(arr):
    res = ''
    for i in arr:
        res += str(i)+'-'
    res = res[:-1]
    return res
