filename = r"C:\Users\sogsquid\Desktop\midlertidig_plassering\munchvrak\backend\auth\queries.py"
file = open(filename)

defs = []
for line in file:
    if line[0:3] == 'def':
        print(line[0:len(line) - 2])

print(*defs)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
