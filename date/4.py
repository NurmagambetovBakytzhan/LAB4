import datetime
x = datetime.datetime(2020, 5, 17)
y = datetime.datetime(2022, 2, 27)
new_date = y - x
print(new_date.total_seconds())