with open("A Tale of Two Citie", "r") as textbook:
    read_file = textbook.readlines()
    a=[]
    for i in read_file:
        a.append((i))
    print(a)
    print(len(a))




