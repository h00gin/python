import time

class TrafficLight:

    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        while True:
            print(f'Цвет светофора: {self.__color[0]}')
            time.sleep(7)
            print(f'Цвет светофора: {self.__color[1]}')
            time.sleep(2)
            print(f'Цвет светофора: {self.__color[2]}')
            time.sleep(7)
            print('Цикл переключения светофора закончен')


a = TrafficLight()
a.running()
