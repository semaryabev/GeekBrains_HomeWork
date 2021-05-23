from itertools import count

for el in count(int(input("Введите чмсло и я покажу все числа начиная с него до 30 :"))):
    if el > 30:
        break
    else:
        print(el)
