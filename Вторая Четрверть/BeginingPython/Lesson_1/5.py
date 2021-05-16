profit = int(input("Введите выручку: "))
cost = int(input("Введите издержку: "))
if profit > cost:
    profitability = (profit - cost) / profit
    print("Вы работаете с прибылью!")
    print("Ваша рентабельность: ",profitability)
    persons = int(input("Введите колличесво сотрудников для расчета прибыли на одного сотрудника: "))
    print("Прибыль на сотрудника состовляет: ",(profit-cost)/persons)
else:
    print("Вы работаете в убыток!")
