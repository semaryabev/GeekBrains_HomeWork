class Road:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.mass = 25
        self.depth = 5

    def calculate(self):
        return self.length*self.width*self.mass*self.depth



a = Road(20,5000)
print(a.calculate())
