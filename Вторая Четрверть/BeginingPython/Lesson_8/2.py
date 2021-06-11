class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

try:
    if b == 0 :
        raise ZeroError('На ноль делить нельзя!')
except ZeroError as err:
    print(err)
else:
    print(a / b)
