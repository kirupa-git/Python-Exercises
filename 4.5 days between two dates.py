import datetime

user_date = datetime.date(1992, 2, 4)
current_date = datetime.date.today()
diff_date = current_date - user_date
print(diff_date.days)
