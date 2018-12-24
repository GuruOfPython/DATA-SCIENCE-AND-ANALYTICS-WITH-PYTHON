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

