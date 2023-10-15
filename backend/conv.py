from datetime import time, date

def time2str(time):
    return str(time.hour) + ':' + str(time.minute) + ':' + str(time.second)

def date2str(date):
    return str(date.year) + ':' + str(date.month) + ':' + str(date.day)