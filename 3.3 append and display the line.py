with open("A Tale of Two Citie", "a+") as textbook:
    txt_line = "this line appended to the tale book file\n"
    for i in range(1):
        textbook.writelines(txt_line)

with open("A Tale of Two Citie", "r") as textbook1:
    last_line = textbook1.readlines()
    la = last_line[-1]
    print(la)
