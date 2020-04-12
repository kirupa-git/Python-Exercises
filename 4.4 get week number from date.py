import datetime

user_date = datetime.date(2015, 6, 16)
print(user_date.__format__("%V"))

print(datetime.date(2015,6,16).isocalendar()[1])




