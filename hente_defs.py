filename = r"C:\Users\sogsquid\Desktop\midlertidig_plassering\munchvrak\backend\auth\queries.py"
file = open(filename)


def get_defs():
    print("\n\nDEFS\n\n")
    for line in file:
        if line[0:3] == 'def':
            print(line[0:len(line) - 2])


def get_classes():
    print("\n\nDEFS\n\n")


get_defs()
