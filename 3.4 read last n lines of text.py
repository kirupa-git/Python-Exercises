with open("A Tale of Two Citie", "r") as textbook1:
    # n is line from last line
    n = 10
    last_line = textbook1.readlines()
    la = lastline[-n:-1]
    print(la)
