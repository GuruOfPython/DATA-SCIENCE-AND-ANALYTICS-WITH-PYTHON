from datetime import datetime

# 1. "{:04d}"
now = datetime.now()
cur_year = now.year
cur_month = now.month
cur_day = now.day

date_str = "{:04d}-{:02d}-{:02d}".format(cur_year, cur_month, cur_day)
print(date_str)

# 2.