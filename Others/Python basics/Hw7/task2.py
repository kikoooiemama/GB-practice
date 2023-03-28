# Реализовать проект расчета суммарного расхода ткани на производство одежды.
from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self):
        pass

    # расход ткани / fabric consumption
    @property
    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return self.fabric_consumption + other.fabric_consumption

    def __str__(self):
        return f"{self.fabric_consumption}"


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 10:
            print("Минимальный размер 10. Установлен минимальный размер.")
            self.__size = 10
        else:
            self.__size = size

    # (V/6.5 + 0.5)
    @property
    def fabric_consumption(self):
        return self.__size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print("Минимальный рост 100. Установлен минимальный рост.")
            self.__height = 100
        else:
            self.__height = height

    # (2*H/100 + 0.3)
    @property
    def fabric_consumption(self):
        return 2 * self.height / 100 + 0.3


coat_size = 52
suit_height = 171
coat = Coat(coat_size)
print(f"Пальто {coat.size} размера: {coat.fabric_consumption:.3f} м. ткани.")
suit = Suit(suit_height)
print(f"Костюм на человека ростом {suit.height} см. : {suit.fabric_consumption:.3f} м. ткани.")
print(f"Костюм и пальто: {coat + suit:.3f} м. ткани.")
