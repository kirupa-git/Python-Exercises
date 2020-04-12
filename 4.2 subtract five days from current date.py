import datetime

current_dt = datetime.datetime.now()
print(current_dt)
delta_date = datetime.timedelta(days=5)
result = current_dt - delta_date
print(result)
