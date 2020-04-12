with open("A Tale of Two Citie", "r") as textbook:
    n = 1
    while n <= 10:
        read_file = textbook.readlines(n)
        print(read_file)
        n = n + 1
