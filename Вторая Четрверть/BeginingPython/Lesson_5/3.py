my_f = open("les3.txt","r")

summ = 0
for line in my_f:
    new_line = line.split()
    if int(new_line[1]) < 20000:
        print(new_line[0])
    summ += int(new_line[1])

print(summ)

my_f.close()
