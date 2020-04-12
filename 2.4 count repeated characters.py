def count_repeatchar(user_input):
    result = {x: user_input.count(x) for x in user_input}

    count = []
    for key, value in result.items():
        if value > 1:
            count.append(key)

    print(f"count of repeated charcters: {len(count)}")


input_char = "repeaters"
count_repeatchar(input_char)
