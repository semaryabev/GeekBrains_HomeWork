my_file = open("les1.txt","w")
while True:
    user_input = input()
    if user_input == '':
        break
    else:
        print(user_input,file=my_file)
my_file.close()
