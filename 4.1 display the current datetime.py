import datetime

current_dt = datetime.datetime.now()
print(current_dt)
current_year = current_dt.__format__("%Y")
print(current_year)
month_year = current_dt.__format__("%m")
print(month_year)
week_number = current_dt.__format__("%U")
print(week_number)
week_day = current_dt.__format__("%u")
print(week_day)
if int(week_day) == 1:
    print("it's Monday")
day_year = current_dt.__format__("%j")
print(day_year)
day_month = current_dt.__format__("%d")
print(day_month)
day_week = current_dt.__format__("%u")
print(day_week)
