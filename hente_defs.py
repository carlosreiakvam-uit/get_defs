import re

input_filname = input("filnavn: ")
re.escape(input_filname)


def get_defs():
    file = open(input_filname)
    print("\n\nMETODER\n")
    for line in file:
        if line[0:3] == 'def':
            print(line[0:len(line) - 2])
    file.close()


def get_classes():
    file = open(input_filname)
    print("\n\nKLASSER\n")
    for line in file:
        if line.__contains__('class'):
            print(line[0:len(line) - 2])
    file.close()


get_defs()
get_classes()
