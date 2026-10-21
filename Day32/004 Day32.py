import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
day=now.day
w=now.weekday()
print(w)
print(year,month,day)


date_of_birth=dt.datetime(year=2003,month=2,day=17,hour=4,minute=17,second=59)
print(date_of_birth)
