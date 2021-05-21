def my_func_1(x,y):
    return x**y

def my_func_2(x,y):
    result = x
    for i in range(1,abs(y)):
        result *= x
    result = 1/result
    return result

x = int(input("Введите х: "))
y = int(input("Введите y: "))

if y > 0:
    print("Вычисление происходит только в отрицательную степень)")
else:
    print(my_func_1(x,y))
    print(my_func_2(x,y))
