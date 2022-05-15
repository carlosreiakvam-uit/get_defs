filename = r"C:\Users\sogsquid\Desktop\midlertidig_plassering\munchvrak\backend\auth\queries.py"
file = open(filename)


def get_defs():
    defs = []
    for line in file:
        if line[0:3] == 'def':
            print(line[0:len(line) - 2])
    print(*defs)

get_defs()
