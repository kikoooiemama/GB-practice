# Реализовать класс Stationery (канцелярская принадлежность).

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationary):
    def draw(self):
        print(f"Отрисовка, используя {self.title}!")


class Pencil(Stationary):
    def draw(self):
        print(f"Отрисовка, используя {self.title}!!")


class Handle(Stationary):
    def draw(self):
        print(f"Отрисовка, используя {self.title}!!!")


stationary = Stationary("Канцелярская принадлежность")
stationary.draw()

pen = Pen("Ручка")
pen.draw()

pencil = Pencil("Карандаш")
pencil.draw()

handle = Handle("Маркер")
handle.draw()
