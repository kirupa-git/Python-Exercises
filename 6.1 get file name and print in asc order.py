import os

with open("D:\Python Exercises/filenames", "r") as textfile:
    with open("D:\Python Exercises/filenames", "w") as textfile1:
        os.chdir("D:/Python Exercises")
        qw = os.getcwd()
        print(qw)
        n = 0
        for i in os.listdir("D:/Python Exercises"):
            n = n + 1
            r1 = textfile1.write("\n")
            r2 = textfile1.write(str(n))
            r3 = textfile1.write(".")
            r4 = textfile1.write(i)

            
            



