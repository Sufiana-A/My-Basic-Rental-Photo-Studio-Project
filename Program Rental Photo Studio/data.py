with open("data.txt", "r") as data:
    for line in data:
        for elem in line.split("`"):
            print(elem)