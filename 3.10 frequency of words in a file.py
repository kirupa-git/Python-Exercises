with open("A Tale of Two Citie", "r") as textbook:
    read_file = textbook.read()
    replace_line = read_file.replace(",", " ")
    next_line = replace_line.replace("\n", " ")
    split_line = next_line.split(" ")
    character_length = []
    for i in split_line:
        character_length.append(i)
    res = {i: character_length.count(i) for i in character_length}
    print(res)
