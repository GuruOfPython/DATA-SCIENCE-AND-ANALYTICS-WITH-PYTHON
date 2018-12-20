from datetime import datetime

# 1. "{:04d}"
now = datetime.now()
cur_year = now.year
cur_month = now.month
cur_day = now.day

date_str = "{:04d}-{:02d}-{:02d}".format(cur_year, cur_month, cur_day)
print(date_str)

# 2. "{:.2f}"

value = "{:.2f}".format(3.1415926)
print(value)
'''
[result] 3.14
'''

value = "{:+.2f}".format(-1)
print(value)
'''
[result] -1.00
'''

value = "{:x<4d}".format(5)
print(value)
'''
[result] 5xxx
'''

value = "{:,}".format(1000000)
print(value)
'''
[result] 1,000,000
'''

value = "{:.2e}".format(1000000000)
print(value)
'''
[result] 1.00e+09
'''

value = "{:10d}".format(13)         # Right aligned (default, width 10)
print(value)
'''
[result]                13
'''

value = "{:<10d}".format(13)        # Left aligned (width 10)
print(value)
'''
[result]        13
'''

value = "{:^10d}".format(13)        # Center aligned (width 10)
print(value)
'''
[result] 13
'''