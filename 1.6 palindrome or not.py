user_input = input("Enter a value:")


def palindrome_func(word):
    sl = user_input
    slt = [user_input]
    re = sl[::-1]
    ret = [re]
    if slt == ret:
        print(f"Entered value {word} is a palindrome")
    elif slt != ret:
        print(f"Entered value {word} is not a palindrome")


palindrome_func(user_input)

