# Создать класс TrafficLight (светофор).
# Для цвета: https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html

from random import choice
import time


class TrafficLight:
    """ Светофор.

    Коды цветов:
     1 - Красный;
     2 - Желтый;
     3 - Зеленый;

     Длительность сигнала:
     Красный - 7 секунд
     Желтый - 2 секунды
     Зеленый - 3 секунды
    """

    def __init__(self):
        self.__color = choice(range(1, 4))

    def out_red(self, text):
        print("\033[31m {}".format(text))

    def out_yellow(self, text):
        print("\033[33m {}".format(text))

    def out_green(self, text):
        print("\033[32m {}".format(text))

    def running(self, switch_times=4):
        correction = 1
        while switch_times > 0:
            if self.__color % 3 == 1:
                self.out_red("Красный")
                correction = 1
                # 7 секунд
                time.sleep(7)
            elif self.__color % 3 == 2:
                self.out_yellow("Желтый")
                # 2 секунды
                time.sleep(2)
            elif self.__color % 3 == 0:
                self.out_green("Зеленый")
                correction = -1
                # 3 секунды
                time.sleep(3)
            self.__color += correction
            switch_times -= 1


trafficLight = TrafficLight()
# print(help(TrafficLight))
try:
    switch_threshold = int(input("Введите количество переключений светофора: \n"))
    if switch_threshold > 0:
        print(f"Установлено ограничение: {switch_threshold} переключения.")
        trafficLight.running(switch_threshold)
    else:
        print("Установлено стандартное ограничение: 4 переключения.")
        trafficLight.running()
except ValueError:
    print("Установлено стандартное ограничение: 4 переключения.")
    trafficLight.running()
