my_list = []
my_list.extend([1,"text",2.4,True,None])
print("Заданый список")
print(my_list)
print("Тип списка")
print(type(my_list))
print("Типы элементов списка")
for el in my_list:
    print(f'{el} \t {type(el)}')
