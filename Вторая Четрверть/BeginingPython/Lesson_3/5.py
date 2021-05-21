print("Вводите числа для суммирования. Если хотите выйти введите q")
result = 0
while True:
    my_list = input().split()
    if "q" in my_list and my_list.index("q") == 0:
        break
    elif "q" not in my_list:
        for i in my_list:
            result += int(i)
    elif "q" in my_list:
        for i in range(0,my_list.index("q")):
            result += int(my_list[i])
        print(result)
        break
    print(result)
