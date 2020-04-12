with open("solar system", "r") as rs:
    with open("solar system_copy", "w") as rw:
        name = []
        for i in rs:
            name.append(i.split("-"))
    print(name)
