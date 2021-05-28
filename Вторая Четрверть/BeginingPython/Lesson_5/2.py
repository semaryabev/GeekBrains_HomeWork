my_f = open("les2.txt","r")

print(f'Всего строк в файле - {len(my_f.readlines())}')

my_f = open("les2.txt","r")

for line in my_f:
    new_line = line.split()
    print(f'{line} - {len(new_line)}')

my_f.close
