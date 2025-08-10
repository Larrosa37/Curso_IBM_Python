### Dates ###

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2026 = datetime(2026, 1, 1,)

print(year_2026)

from datetime import time

current_time = time()

print_date(current_time)