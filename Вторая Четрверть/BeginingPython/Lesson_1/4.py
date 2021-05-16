n = int(input("Введите целое число: "))
max = -1
while n>0:
    if n % 10 > max:
        max = n % 10
    n = n // 10
print("Максимальное цифра в числе: ",max)
