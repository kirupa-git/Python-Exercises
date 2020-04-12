try:
    import datetime
    import re


    def greet_message(name, age):
        print(f"Hi, {name} Welcome to Mashupstack!")

        cal_year = 100 - age
        current_year = datetime.datetime.now().year

        print(f"we wish you a long live, You turnout 100 "
              f"years in the year {current_year + cal_year}")


    user_name = input("Enter your name:")
    x = re.findall("[a-zA-Z]", user_name)
    if x:
        user_age = int(input("Enter your age:"))

    greet_message(user_name, user_age)

except NameError:
    print("Please enter a valid Name ")
except ValueError:
    print("Please enter a valid age ")
