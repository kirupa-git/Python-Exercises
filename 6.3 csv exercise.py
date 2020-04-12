import csv

with open("6.3_csv file.csv", "r") as test:
    store = []
    for i in test:
        store.append(i)
    print("3rd row of csv file")
    print(store[3])
    print("2nd column of csv file")
    csv_reader = csv.reader(store)
    for i in csv_reader:
        print(i[1])
    print("\n\n")
    print("first 3 lines of csv file")
    ww = store[0:3]
    for i in ww:
        print(i, end="")
