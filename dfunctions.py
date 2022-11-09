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
