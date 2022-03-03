import datetime

x = datetime.datetime.now() 
day = datetime.timedelta(1)
yesterday = x - day
tomorrow = x + day
print(f'yesterday: {yesterday.strftime("%x")}')
print(f'today: {x.strftime("%x")}')
print(f'tomorrow: {tomorrow.strftime("%x")}')