def n_terms(n):
    if n < 1:
        return 0
    else:
        return n + n_terms(n - 2)


result = n_terms(-2)
print(result)
