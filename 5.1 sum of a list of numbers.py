num_list = [1, 2, 3, 4, 5, 6]


def sum_num(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum_num(list[1:])


print(sum_num(num_list))
