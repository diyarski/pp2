import datetime
today=datetime.date.today()
delta=datetime.timedelta(days=1)
yesterday=today-delta
tomorrow=today+delta
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
