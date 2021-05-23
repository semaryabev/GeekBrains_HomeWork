from sys import argv

def salary_calculate(t,s,p):
    return t*s+p

f,work_time, work_bet, bonus = argv
print(f'Зарплата составляет : {salary_calculate(int(work_time),int(work_bet),int(bonus))}')
