dict_num1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key_dict = []
values_dict = []
items_dict = []


def get_items(dict_num, *args):

    for i in dict_num.keys():
        key_dict.append(i)
    print(f"keys: {key_dict}")

    for i in dict_num.values():
        values_dict.append(i)
    print(f"Values: {values_dict}")

    for i in dict_num.items():
        items_dict.append(i)
    print(f"items:{items_dict}")


get_items(dict_num1)
