import re

input_filname = input("filnavn: ")
filename = r"C:\Users\sogsquid\Desktop\midlertidig_plassering\munchvrak\backend\weekly_menu\views.py"
re.escape(filename)


def get_defs():
    file = open(filename)
    print("\n\nMETODER\n")
    for line in file:
        if line[0:3] == 'def':
            print(line[0:len(line) - 2])
    file.close()


def get_classes():
    file = open(filename)
    print("\n\nKLASSER\n")
    for line in file:
        if line.__contains__('class'):
            print(line[0:len(line) - 2])
    file.close()


get_defs()
get_classes()
