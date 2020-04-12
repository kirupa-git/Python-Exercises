with open("A Tale of Two Citie", "r") as textbook:
    read_line = textbook.read()
    replace_line = read_line.replace(",", " ")
    next_line = replace_line.replace("\n", " ")
    split_line = next_line.split(" ")
    character_length = []
    for i in split_line:
        character_length.append(i)
    character_length.sort(key=len)
    print(max(character_length, key=len))
