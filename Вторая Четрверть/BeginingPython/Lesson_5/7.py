import json

my_dict = {}
avr_profit = 0
avr_profit_count = 0

with open("les7.txt","r") as my_f:
    for line in my_f:
        my_l = line.split()
        profit = int(my_l[2]) - int(my_l[3])
        if profit > 0:
            avr_profit += profit
            avr_profit_count += 1
        my_dict.update({my_l[0]:profit})

new_list = [my_dict,{'average_profit':avr_profit/avr_profit_count}]

with open("les7_answ.json","w") as my_json_answ:
    json.dump(new_list,my_json_answ)
