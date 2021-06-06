from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def __init__(self, param):
        pass

    @abstractmethod
    def calculate(self):
        pass

class Coat(MyAbstractClass):

    def __init__(self, param):
        self.param = int(param)
    @property
    def calculate(self):
        return self.param / 6.5 + 0.5


class Costume(MyAbstractClass):

    def __init__(self, param):
        self.param = int(param)

    @property
    def calculate(self):
        return 2 * self.param + 0.3


coat = Coat(56)
costume = Costume(1.8)
print(coat.calculate)
print(costume.calculate)
