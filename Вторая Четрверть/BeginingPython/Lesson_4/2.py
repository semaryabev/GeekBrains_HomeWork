my_list = [300,2,12,44,1,1,4,10,7,1,78,123,55,56,44,101]
new_list = [my_list[i+1] for i in range(0,len(my_list)-1) if my_list[i+1] > my_list[i]]
print(new_list)
