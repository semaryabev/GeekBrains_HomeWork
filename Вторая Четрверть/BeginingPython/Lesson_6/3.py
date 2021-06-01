class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage":wage,"bonus":bonus,"total":bonus+wage}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income.get("total"))



p = Position("alex","ivanov","lead",100,50)
p.get_full_name()
p.get_total_income()
