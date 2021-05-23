from functools import reduce

def my_composition(a,b):
    return a*b

my_list = [el for el in range(100,1001) if el % 2 == 0]
print(reduce(my_composition, my_list))
