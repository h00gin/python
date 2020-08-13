class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        self.direction = direction
        print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна: {self.speed} км')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна: {self.speed} км')
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} превышена на: {self.speed - 60} км')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна : {self.speed} км')
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} превышена на: {self.speed - 40} км')


class PoliceCar(Car):
    pass


# town_car = TownCar(85, 'Black', 'Chevrolet', False)
# print (town_car.name)
# town_car.go()
# town_car.stop()
# town_car.turn('налево')
# town_car.show_speed()

# police_car = PoliceCar(85, 'Белый', 'ВАЗ', True)
# print(police_car.color)
#
# police_car.go()
# police_car.turn('вправо')
# police_car.show_speed()

# work_car = WorkCar(65, 'asывda', 'Hino', 'asda')
# print(work_car.stop())
# work_car.show_speed()
