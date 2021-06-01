from time import sleep

class TrafficLight:

    __color = ''

    def running(self):
        color = 'красный'
        print(color)
        sleep(7)
        color = 'желтый'
        print(color)
        sleep(3)
        color = 'зеленый'
        print(color)
        sleep(10)


a = TrafficLight()
a.running()
