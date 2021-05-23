from itertools import cycle

c = 1
my_list = input('Введите список и я повторю его элементы 15 раз: ').split()
for el in cycle(my_list):
    if c > 15:
        break
    print(el)
    c += 1

