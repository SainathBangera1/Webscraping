import datetime

# input = 'Monday December 14, 2020 4:00 PM '
# output = [14, 12, 2020, 4]
calender = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
def RDate(strData):
    st = strData.split(" ")
    arr = [int(st[2].replace(',','')),calender[st[1]],int(st[3]),int(st[4][0])]
    return arr

# input = [27,2,2023]
def checkDate(arr):
    res=''
    try:
        res = datetime.datetime(year=arr[2],month=arr[1],day=arr[0])
    except ValueError:
        res = False
    return res


base = datetime.datetime.today()
print(base)
# date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
