my_f = open("les4.txt","r")

my_dict = dict(One='Один', Two='Два', Three='Три', Four='Четыре')


new_f = open("les4_ans.txt","w")

for line in my_f:
    new_line = line.split(" - ")
    print(f'{my_dict.get(new_line[0])} - {new_line[1]}',file = new_f)

my_f.close()
new_f.close()
