class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car is go')

    def stop(self):
        print('Car is stop')

    def turn(self, to_turn):
        print(f'Car is turn {to_turn}')

    def show_speed(self):
        print(f'Car speed {self.speed}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            print(f'Town Car speed = {self.speed}. OK')
        else:
            print(f'Town Car speed = {self.speed}. Speed Violation')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 40:
            print(f'Work Car speed = {self.speed}. OK')
        else:
            print(f'Work Car speed = {self.speed}. Speed Violation')

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)




police_car = PoliceCar(70,'blue','BMW', True)
work_car_1 = WorkCar(39,'red','opel', False)
sport_car = SportCar(90,'orange','kia', False)
town_car_1 = TownCar(59,'green','lada', False)
town_car_2 = TownCar(65,'metalic','fiat', False)
work_car_2 = WorkCar(45,'white','ford', False)

print(police_car.name)
print(work_car_1.color)
print(town_car_1.is_police)

work_car_1.show_speed()
work_car_2.show_speed()
town_car_1.show_speed()
town_car_2.show_speed()
sport_car.show_speed()
