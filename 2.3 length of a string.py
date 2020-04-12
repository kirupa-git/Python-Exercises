input_message = "moneyheist"


def len_str(user_input):
    len_string = []

    for i in range(len(user_input)):
        (len_string.append(i + 1))

    print(len_string[-1])


len_str(input_message)
