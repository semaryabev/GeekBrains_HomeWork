class Data:

    str_data = ''
    my_list = []

    def __init__(self, data):
        Data.str_data = data
        #Data.my_list = []

    @classmethod
    def pars(cls):
        cls.my_list = []
        cls.my_list.extend(int(el) for el in cls.str_data.split('-'))
        return cls.my_list
        
    @staticmethod
    def valid(my_list1):
        day = False
        mounth = False
        year = False

        if my_list1[1] >= 1 and my_list1[1] <= 12:
            mounth = True

        if my_list1[2] > 0:
            year = True

        if my_list1[0] >=1 and my_list1[0] <= 30 and my_list1[1] in [4,6,9,11]:
            day = True
        
        elif my_list1[0] >=1 and my_list1[0] <= 31 and my_list1[1] in [1,3,5,7,8,10,12]:
            day = True

        elif my_list1[0] >=1 and my_list1[0] <= 28 and my_list1[1] == 2:
            day = True

        elif my_list1[0] >=1 and my_list1[0] <= 29 and my_list1[1] == 2 and my_list1[2] % 4 == 0:
            day = True

        print(f'day - {day}\nmounth - {mounth}\nyear - {year}\n')


print('20-8-2020')
Data.valid(Data('20-8-2020').pars())
print('32-8-2020')
Data.valid(Data('32-8-2020').pars())
print('29-2-2020')
Data.valid(Data('29-2-2020').pars())
print('29-2-2019')
Data.valid(Data('29-2-2019').pars())

print('30-2-2008')
Data.valid(Data('30-2-2008').pars())

print('0-0-0')
Data.valid(Data('0-0-0').pars())

print('119-155-2019')
Data.valid(Data('119-155-2019').pars())

print('76-32-0')
Data.valid(Data('76-32-0').pars())

