class Cage:

    def __init__(self, cage_count_cell):
        self.cage_count_cell = cage_count_cell
    
    def __add__(self, other):
        return Cage(self.cage_count_cell + other.cage_count_cell)

    def __sub__(self, other):
        if self.cage_count_cell - other.cage_count_cell < 0:
            return print(f'Не возможно вычетание! Результат меньше нуля')
        else:
            return Cage(self.cage_count_cell - other.cage_count_cell)

    def __mul__(self, other):
        return Cage(self.cage_count_cell * other.cage_count_cell)

    def __floordiv__(self, other):
        return Cage(self.cage_count_cell // other.cage_count_cell)

    def __str__(self):
        return f'Result: {self.cage_count_cell}'

    def make_order(self, cage_count_in_row):
        string_return = ''
        a = self.cage_count_cell // cage_count_in_row
        b = self.cage_count_cell % cage_count_in_row
        for i in range(a):
            for j in range(cage_count_in_row):
                string_return += '*'
            string_return += r'\n'

        for i in range(b):
            string_return += '*'

        return string_return



cage1 = Cage(50)
cage2 = Cage(21)
cage3 = Cage(22)

print(cage1 + cage2)
print(cage1 - cage2)
print(cage1 * cage2)
print(cage1 // cage2)
print(cage2 - cage3)

print(cage1.make_order(10))
print(cage2.make_order(20))

