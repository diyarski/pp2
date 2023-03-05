import datetime
now = datetime.datetime.now()
now = now.replace(microsecond=0)
print(now)
