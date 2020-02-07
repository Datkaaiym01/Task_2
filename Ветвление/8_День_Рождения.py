import datetime
import calendar

d, m = map(int, input().split())
date_ = datetime.date(2016, m, d)
print(calendar.day_name[date_.weekday()])