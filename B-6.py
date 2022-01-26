list_men = input("サイコロの面の数は？: ")
list_kai = input("何回振りますか？: ")

import random


def dice(app):
    return random.randint(1, int(app))


aka = []
for rin in range(int(list_kai)):
    aka.append(str(random.randint(1, int(dice(list_men)))))

print(aka)
