my_list = [7,5,3,3,2]

print("Вводите числа для пополнения рейтинга. Если хотите завершить введите -1")
while True:
    user_input = int(input())
    if user_input == -1:
        break
    else:
        my_list.append(user_input)
        my_list.sort(reverse=True)
        print(f'Новый рейнинг: {my_list}')
