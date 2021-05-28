new_f = open("les5.txt","w")

new_f.write("23 45 66 1 33 41 6 7 4 3 21 5")

new_f.close()

summ = 0

with open("les5.txt") as my_f:
    my_l = my_f.readline().split()
    for el in my_l:
        summ += int(el)

print(summ)
