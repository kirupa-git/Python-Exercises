try:
    user_input = float(input("Enter a Number:"))


    def check_number(number):
        if user_input % 2 == 0:
            print(f"Entered number {number} is even number")
        else:
            print(f"Entered number {number} is a odd number")


    check_number(user_input)

except ValueError:
    print("Please enter a valid Number ")
