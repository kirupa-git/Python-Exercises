with open("A Tale of Two Citie", "r") as textbook:
    read_file = textbook.readlines()
    store = []
    for line in read_file:
        store.append(line)
    print(store, end="")