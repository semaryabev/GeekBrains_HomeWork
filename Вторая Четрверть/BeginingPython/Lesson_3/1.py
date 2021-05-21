def my_func():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if b == 0:
        print("На ноль делить нельзя. Введите числа занаво")
        my_func()
    else:
        return print(f'{a} / {b} = {a/b}')

my_func()
