import datetime
x = datetime.datetime.now() 
a = datetime.timedelta(5)
new_date = x - a
print(new_date.strftime("%x"))