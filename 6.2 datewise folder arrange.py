import os

os.chdir("C:/Users/KP s Dell/Desktop/Python Exercises/Exercise_set#6/datewise")

# with open("C:/Users/KP s Dell/Desktop/Python Exercises/Exercise_set#6/datewise/01012020.txt", "w+") as textfile:
#     list1 = range(2, 12)
#     for i in list1:
#         open('010%s2020.txt' % i, 'w').write(" ")
#

for i in os.listdir("C:/Users/KP s Dell/Desktop/Python Exercises/Exercise_set#6/datewise"):
    f_empty, f_type = os.path.split(i)
    f_name, f_ext = f_type.split(".")
    ff = f_name[2]
    ff1 = f_name[3]
    fs = ff + ff1
    if "01" in fs:
        print(f"jan-{i}")
    elif"02" in fs:
        print(f"feb-{i}")
    elif "03" in fs:
        print(f"mar-{i}")
    elif "04" in fs:
        print(f"apr-{i}")
    elif "05" in fs:
        print(f"may-{i}")
    elif "06" in fs:
        print(f"june-{i}")
    elif "07" in fs:
        print(f"july-{i}")
    elif "08" in fs:
        print(f"Aug-{i}")
    elif "09" in fs:
        print(f"sep-{i}")
    elif "10" in fs:
        print(f"OCt-{i}")
    elif "11" in fs:
        print(f"Nov-{i}")
    elif "12" in fs:
        print(f"Dec-{i}")
