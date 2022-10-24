import datetime

weekdays = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]


def date_Day(dd, mm, yy):
    tday = datetime.date(yy, mm, dd)
    return weekdays[tday.isoweekday()]
