# Реализуйте базовый класс Car.
from random import choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name} поехал!")

    def stop(self):
        print(f"Автомобиль {self.name} остановился!")

    def turn(self, direction):
        print(f"Автомобиль {self.name} повернул {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name}: {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости у {self.name}!")
        else:
            print(f"Скорость {self.name}: {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости у {self.name}!")
        else:
            print(f"Скорость {self.name}: {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


directions = ["налево", "напрвао"]
town_car = TownCar(65, "Черный", "Ford Focus")
print(f"Название: {town_car.name}")
print(f"Цвет: {town_car.color}")
print(f"Скорость: {town_car.speed}")
print(f"Это полицейский автомобиль? {'Да' if town_car.is_police else 'Нет'}")
town_car.go()
town_car.stop()
town_car.turn(choice(directions))
town_car.show_speed()
print(f"{'-' * 35}")

sport_car = SportCar(155, "Желтый", "BMW M4")
print(f"Название: {sport_car.name}")
print(f"Цвет: {sport_car.color}")
print(f"Скорость: {sport_car.speed}")
print(f"Это полицейский автомобиль? {'Да' if sport_car.is_police else 'Нет'}")
sport_car.go()
sport_car.stop()
sport_car.turn(choice(directions))
sport_car.show_speed()
print(f"{'-' * 35}")

work_car = WorkCar(45, "Белый", "УАЗ")
print(f"Название: {work_car.name}")
print(f"Цвет: {work_car.color}")
print(f"Скорость: {work_car.speed}")
print(f"Это полицейский автомобиль? {'Да' if work_car.is_police else 'Нет'}")
work_car.go()
work_car.stop()
work_car.turn(choice(directions))
work_car.show_speed()
print(f"{'-' * 35}")

police_car = PoliceCar(120, "Синий", "Porsche 911")
print(f"Название: {police_car.name}")
print(f"Цвет: {police_car.color}")
print(f"Скорость: {police_car.speed}")
print(f"Это полицейский автомобиль? {'Да' if police_car.is_police else 'Нет'}")
police_car.go()
police_car.stop()
police_car.turn(choice(directions))
police_car.show_speed()
print(f"{'-' * 35}")
