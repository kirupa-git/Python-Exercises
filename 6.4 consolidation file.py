import csv
import os

print(os.getcwd())
with open("01022017_consolidation.csv", "w+") as consolidation:
    my_list = range(0, 18)
    # portion to create a file with fileheaders and contents
    for i in my_list:
        open("01022017_%s.csv" % i, "w").write(
            "id,date,location,car name,model name,seller name,seller address,price\n")
        open("01022017_%s.csv" % i, "a").write(
            "%s,04/02/2020,trivandrum,Toyota,Etios,kirupaagar,Kazhakootam,7,00,000\n" % i)

    new = []
    for i in my_list:
        with open("01022017_%s.csv" % i, "r")as text:
            new.append(text.read())

    for i in new:
        consolidation.write(i)

