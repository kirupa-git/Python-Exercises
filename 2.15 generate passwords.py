import random
import string


def password_gen():
    username = input("Enter Username:")
    charac_string = string.ascii_lowercase + string.ascii_uppercase + string.punctuation

    rand_char = random.choice(charac_string)

    password = "".join(random.choice(charac_string) for i in range(9))

    return print(f"user password is {password}")


password_gen()
