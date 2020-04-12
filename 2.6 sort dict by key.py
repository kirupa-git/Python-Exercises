color_dict = {
    "red": "#FF0000",
    "green": "#008000",
    "black": "#000000",
    "white": "#FFFFFF"
}

result = {}


def sort_dict(sorting):
    for key in sorted(sorting):
        result.update({key: sorting[key]})

    return result


print(sort_dict(color_dict))
