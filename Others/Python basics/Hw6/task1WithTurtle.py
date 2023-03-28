# Создать класс TrafficLight (светофор).

import turtle
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

    def running(self, switch_times=4):
        pen = turtle.Turtle()
        pen.color('black')
        pen.width(3)
        pen.hideturtle()

        pen.penup()
        pen.setposition(-40, 100)
        pen.pendown()
        pen.forward(80)
        pen.right(90)
        pen.forward(200)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
        pen.forward(200)

        red_light = turtle.Turtle()
        red_light.shape('circle')
        red_light.shapesize(2)
        red_light.color('grey')
        red_light.penup()
        red_light.setposition(0, 60)

        yellow_light = turtle.Turtle()
        yellow_light.shape('circle')
        yellow_light.shapesize(2)
        yellow_light.color('grey')
        yellow_light.penup()
        yellow_light.setposition(0, 0)

        green_light = turtle.Turtle()
        green_light.shape('circle')
        green_light.shapesize(2)
        green_light.color('grey')
        green_light.penup()
        green_light.setposition(0, -60)

        correction = 1
        while switch_times > 0:
            if self.__color % 3 == 1:
                red_light.color('red')
                correction = 1
                # 7 секунд
                time.sleep(7)
                red_light.color('grey')
            elif self.__color % 3 == 2:
                yellow_light.color('yellow')
                # 2 секунды
                time.sleep(2)
                yellow_light.color('grey')
            elif self.__color % 3 == 0:
                green_light.color('green')
                correction = -1
                # 3 секунды
                time.sleep(3)
                green_light.color('grey')
            self.__color += correction
            switch_times -= 1


trafficLight = TrafficLight()
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
print("Программа завершила свою работу!")
