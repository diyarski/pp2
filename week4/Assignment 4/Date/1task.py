import datetime
current_date=datetime.date.today()
delta=datetime.timedelta(days=5)
result_date=current_date-delta
print("Current date:", current_date)
print("Result date:", result_date)
