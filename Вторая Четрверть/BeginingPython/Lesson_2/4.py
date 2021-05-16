my_list = input("Введите строку: ").split()
for ind, el in enumerate(my_list,1):
    print(ind, el) if len(el) <= 10 else print(ind, el[0:10])
