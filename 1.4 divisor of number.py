try:
    user_input = int(input("Enter a Number:"))

    range_number = range(1, user_input)

    divider_output = []
    for i in range_number:
        if user_input % i == 0:
            divider_output.append(i)

    print(f"Dividers of {user_input} are {divider_output}")

except ValueError:
    print("Please enter a valid Number ")

