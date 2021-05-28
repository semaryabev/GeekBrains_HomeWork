my_list = ['(',')','л','п','р','а','б','-']
my_dict = {}

with open("les6.txt","r") as my_f:
    for line in my_f:
        summ = 0
        new_l = line.split(': ')
        my_str = new_l[1].translate({ord(i): None for i in my_list}).split()
        for el in my_str:
            summ += int(el)
        my_dict.update({new_l[0]:summ})


print(my_dict)
