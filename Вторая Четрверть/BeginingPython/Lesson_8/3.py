class MyExceptionClass(Exception):
    def __init__(self, text, el):
        self.text = text
        self.el = el

my_list = []
print('Запоните список числами! Для завершения введите "stop"')
while True:
    inp_data = input('Введите число: ')
    if inp_data == 'stop':
        break

    try:
        #my_list.extend(int(el) for el in inp_data.split() if el.isnumeric() == True)
        for el in inp_data.split():
            if el.isnumeric() == True:
                my_list.append(int(el))
            else:
                raise MyExceptionClass('Нужно вводить числа!', el)
    except MyExceptionClass as err:
        print(f'{err.text} {err.el} - не число!')

print(my_list)
