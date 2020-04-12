with open("A Tale of Two Citie", "r") as textbook:
    with open("A Tale of Two Citie_copy", "w") as textbookc:
        read_file = textbook.read()
        for i in read_file:
            textbookc.write(i)

with open("A Tale of Two Citie_copy", "r") as textbookr:
    reading_file = textbookr.read()
    print(reading_file)
