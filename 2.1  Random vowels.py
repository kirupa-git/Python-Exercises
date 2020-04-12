import itertools
vowels_list = ["a", "e", "i", "o", "u"]
iter_format = itertools.permutations(vowels_list)

for x in iter_format:
    print(("".join(x)))
