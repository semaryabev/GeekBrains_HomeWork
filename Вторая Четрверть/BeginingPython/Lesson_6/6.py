class Stationery:

    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')

class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')

class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')


pen = Pen('I`m a pen')
pencil = Pencil('I`m an Apple pencil')
handle = Handle('I`m a handle')
paper = Stationery('I`m not ...')

pen.draw()
pencil.draw()
handle.draw()
paper.draw()
