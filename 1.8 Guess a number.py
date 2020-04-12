try:
    import random
    input_number = int(input("Guess a Number(0-9):"))

    def guess_number(user_input):
        range_input = range(0, 10)
        if user_input not in range_input:
            print("Enter a number between 0 and 9")
        else:
            lucky_number = random.randrange(0, 9)
            print(f"Lucky Number:{lucky_number}")
            for i in range_input:
                while i == user_input:
                    if user_input < lucky_number:
                        print("Guessed number is too low")
                    elif user_input > lucky_number:
                        print("Guessed number is too High")
                    else:
                        print("Your Guess is Right")
                    break

    guess_number(input_number)

except ValueError:
    print("Enter a number between 0 and 9")
