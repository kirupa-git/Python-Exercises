from itertools import combinations

my_list = ["x", "y", "z"]
sub = []
for i in range(len(my_list) + 1):
    combo = [list(x) for x in combinations(my_list, i)]
    sub.extend(combo)
print(sub)
