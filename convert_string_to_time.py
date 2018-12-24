from datetime import datetime

cur_time = datetime.now()
print(cur_time)

cur_year = cur_time.year
cur_month = cur_time.month
cur_day = cur_time.day

first_day = datetime(cur_year, cur_month, 1)
print(first_day)

dt = datetime.strptime('2018-12-25', '%Y-%m-%d')

print(dt < first_day)

str = "Dec 3, 2018"
import re
match = re.findall(r"([A-Za-z]+)\s?([0-9]+),\s?([0-9]+)", str)[0]
print(match)
