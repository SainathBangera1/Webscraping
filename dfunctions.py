import datetime
from datetime import datetime as dt

weekdays = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]


def date_Day(dd, mm, yy):
    tday = datetime.date(yy, mm, dd)
    return weekdays[tday.isoweekday()]


def deltaDays(date1, date2):
    res = (dt.strptime(date1, "%Y/%m/%d") -
           dt.strptime(date2, "%Y/%m/%d")).days
    return res
