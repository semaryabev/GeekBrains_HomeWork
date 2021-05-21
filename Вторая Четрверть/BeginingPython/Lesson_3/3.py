def my_func(a,b,c):
    '''Вычисляет сумму 2-х наибольших чисел из 3-х'''
    new_list = [a, b, c]
    new_list.sort(reverse=True)
    return print(f'Сумма двух максимальных {new_list[0]} + {new_list[1]} = {new_list[0] + new_list[1]}')

a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
my_func(a,b,c)
