dicone = {1: 10, 2: 20}
dictwo = {3: 30, 4: 40}
dicthree = {5: 50, 6: 60}


def merge_dict(*args):
    result = {}
    for x in args:
        result.update(x)
    return result


merger = merge_dict(dictwo, dicone, dicthree)


def sort_dict(merging):
    sorter = {}
    for i in sorted(merging):
        sorter.update({i: merging[i]})

    print(sorter)


sort_dict(merger)
