with open("A Tale of Two Citie","r") as textbook1:
    with open("A Tale of Two Citie", "w") as textbook:
        list_items = ["Every", " ", "word", "in", "the", "list", "is", "added", "to"]
        for i in list_items:
            textbook.writelines(i)
    print(textbook1.read())


