# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру (например, словарь).

# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Проект 'Склад'
from abc import ABC, abstractmethod


class MyIncorrectParameterError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self):
        # self.__warehouse = {str(key): {Scanner.valid_constructor("Canon A2", "white"): 2,
        #                                Printer.valid_constructor("HP Pro", "black", 4): 4} for key in
        #                     OfficeEquipment.__subclasses__()}
        self.__warehouse = {str(key): {} for key in OfficeEquipment.__subclasses__()}

    def send_to_warehouse(self, send_equipment, send_amount=1):
        key = str(type(send_equipment))
        value_dict = dict(self.__warehouse.get(key))
        if list(value_dict.keys()).count(send_equipment) > 0:
            value_dict[send_equipment] = value_dict.get(send_equipment) + send_amount
            print("На склад поступила новая партия уже имеющегося оборудования!")
        else:
            value_dict.update({send_equipment: send_amount})
            print("На склад поступил новый товар!")
        self.__warehouse[key] = value_dict

    def take_from_warehouse(self, take_equipment, take_amount=1):
        key = str(type(take_equipment))
        value_dict = dict(self.__warehouse.get(key))
        if list(value_dict.keys()).count(take_equipment) > 0:
            how_much = value_dict.get(take_equipment)
            if how_much <= take_amount:
                value_dict.pop(take_equipment)
                print(f"На складе было [{take_equipment}] в количестве {how_much}.\n"
                      f"По заявке удалось забрать {how_much} шт. и на складе больше не осталось данного оборудования.")
            else:
                value_dict[take_equipment] = how_much - take_amount
                print(f"На складе было [{take_equipment}] в количестве {how_much}.\n"
                      f"По заявке удалось забрать {take_amount} шт. "
                      f"и на складе еще осталось {how_much - take_amount} шт. данной техники.")
            self.__warehouse[key] = value_dict
        else:
            print("К сожалению запрашиваемое оборудование отсутствует на складе!\n"
                  "Ожидайте когда оно снова поступит на склад")

    def show_equipment(self, equipment):
        print(self.__warehouse.get(type(equipment)))

    @property
    def get_warehouse(self):
        return self.__warehouse

    def __str__(self):
        s = ""
        for k, v in self.__warehouse.items():
            if k == "<class '__main__.Printer'>":
                s += "Принтеры:\n"
            elif k == "<class '__main__.Scanner'>":
                s += "Сканеры:\n"
            elif k == "<class '__main__.Xerox'>":
                s += "Ксероксы:\n"
            i = 1
            for n, m in v.items():
                s += f"    {i}. {n} | {m} шт.\n"
                i += 1
        return s


class OfficeEquipment(ABC):
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    @abstractmethod
    def valid_constructor(self, param1, param2, param3):
        pass


class Printer(OfficeEquipment):
    def __init__(self, model, color, type_printer, name="Принтер"):
        super().__init__(name, model, color)
        self.type_printer = type_printer

    @classmethod
    def valid_constructor(cls, model, color, type_printer, name="Принтер"):
        source = {1: "Лазерный", 2: "Светодиодный", 3: "Струйный", 4: "Матричный", 5: "3-D"}
        if str(type_printer).isdigit():
            if int(type_printer) < 1 or int(type_printer) > 5:
                raise MyIncorrectParameterError("Некорректное значение для вида принтера.")
            else:
                type_printer = source.get(int(type_printer))
        else:
            raise MyIncorrectParameterError("Некорректное значение для вида принтера.")
        return Printer(model, color, type_printer, name)

    def __str__(self):
        return f"{self.name} {self.model} (цвет: {self.color}, вид принтера: {self.type_printer})"

    def __eq__(self, other):
        if self.model == other.model and self.color == other.color and self.type_printer == other.type_printer and \
                self.name == other.name:
            return True
        else:
            return False

    def __key(self):
        return self.model, self.color, self.type_printer, self.name

    def __hash__(self):
        return hash(self.__key())


class Scanner(OfficeEquipment):
    def __init__(self, model, color, max_format="A4", name="Сканер"):
        super().__init__(name, model, color)
        self.max_format = max_format

    @classmethod
    def valid_constructor(cls, model, color, max_format="A4", name="Сканер"):
        if max_format.startswith("А"):
            # на латинице и на кирилице
            max_format = max_format.replace("А", "A")
        if max_format.startswith("A"):
            number = max_format[1:]
            if number.isdigit():
                if int(number) < 0 or int(number) > 10:
                    raise MyIncorrectParameterError("Формат листов строго от А0 до А10.")
            else:
                raise MyIncorrectParameterError("В формате после 'А' должно быть число.")
        else:
            raise MyIncorrectParameterError("Формат должен начинаться с буквы 'А'.")

        return Scanner(model, color, max_format, name)

    def __str__(self):
        return f"{self.name} {self.model} (цвет: {self.color}, макс. формат: {self.max_format})"

    def __eq__(self, other):
        if self.model == other.model and self.color == other.color and self.max_format == other.max_format and \
                self.name == other.name:
            return True
        else:
            return False

    def __key(self):
        return self.model, self.color, self.max_format, self.name

    def __hash__(self):
        return hash(self.__key())


class Xerox(OfficeEquipment):
    def __init__(self, model, color, copy_speed, name="Ксерокс"):
        super().__init__(name, model, color)
        self.copy_speed = copy_speed

    @classmethod
    def valid_constructor(cls, model, color, copy_speed, name="Ксерокс"):
        if str(copy_speed).isdigit():
            i = int(copy_speed)
            if i < 1 or i > 50:
                raise MyIncorrectParameterError("Нереалистичная скорость копирования для ксерокса.")
        else:
            raise MyIncorrectParameterError("Скорость копирования для ксерокса должно быть числом.")

        return Xerox(model, color, int(copy_speed), name)

    def __str__(self):
        return f"{self.name} {self.model} (цвет: {self.color}, скорость копирования: {self.copy_speed} лист/мин)"

    def __eq__(self, other):
        if self.model == other.model and self.color == other.color and self.copy_speed == other.copy_speed and \
                self.name == other.name:
            return True
        else:
            return False

    def __key(self):
        return self.model, self.color, self.copy_speed, self.name

    def __hash__(self):
        return hash(self.__key())


def input_subcommands():
    subcommands = ("1", "2", "3", "q")
    while True:
        print(f"\nВыберите оборудование, введя одну из следующих команд:"
              f"\n{subcommands[0]:<2} - принтеры"
              f"\n{subcommands[1]:<2} - сканеры"
              f"\n{subcommands[2]:<2} - ксероксы"
              f"\n{subcommands[3]:<2} - для отмены операции")
        subcommand = input("\nВведите команду: ")
        if subcommand == "q" or subcommand == "'q'":
            print("Отмена операции")
            return None
        elif subcommand == "1":
            sub_model = input("Укажите модель принтера: ")
            sub_color = input("Укажите цвет принтера: ")
            sub_type_printer = input("Укажите вид принтера введя 'ЧИСЛО', соответствующее словарю\n{1: Лазерный,"
                                     " 2: Светодиодный, 3: Струйный, 4: Матричный, 5: 3-D}: ")
            sub_amount = input("Укажите количество принтеров (число):")
            if not sub_amount.isdigit():
                print("Введено некоректное количество принтеров. Попробуйте сначала!")
                continue
            else:
                try:
                    printer = Printer.valid_constructor(sub_model, sub_color, sub_type_printer)
                except MyIncorrectParameterError as sub_err:
                    print(f"Ошибка: {sub_err}\nПопробуйте снова!")
                    continue
                else:
                    return printer, int(sub_amount)
        elif subcommand == "2":
            sub_model = input("Укажите модель сканера: ")
            sub_color = input("Укажите цвет сканера: ")
            sub_format = input("Укажите максимальный формат листа (А0-А10) для сканера: ")
            sub_amount = input("Укажите количество сканеров (число):")
            if not sub_amount.isdigit():
                print("Введено некоректное количество сканеров. Попробуйте сначала!")
                continue
            else:
                try:
                    scanner = Scanner.valid_constructor(sub_model, sub_color, max_format=sub_format)
                except MyIncorrectParameterError as sub_err:
                    print(f"Ошибка: {sub_err}\nПопробуйте снова!")
                    continue
                else:
                    return scanner, int(sub_amount)
        elif subcommand == "3":
            sub_model = input("Укажите модель ксерокса: ")
            sub_color = input("Укажите цвет ксерокса: ")
            sub_copy_speed = input("Укажите скорость копирования (лист/мин - число) для ксерокса: ")
            sub_amount = input("Укажите количество ксероксов (число):")
            if not sub_amount.isdigit():
                print("Введено некоректное количество ксероксов. Попробуйте сначала!")
                continue
            else:
                try:
                    xerox = Xerox.valid_constructor(sub_model, sub_color, sub_copy_speed)
                except MyIncorrectParameterError as sub_err:
                    print(f"Ошибка: {sub_err}\nПопробуйте снова!")
                    continue
                else:
                    return xerox, int(sub_amount)
        else:
            print("Неизвестная команда при выборе оборудования. Попробуйте снова!")


# xerox = Xerox.valid_constructor("Canon-123", "black", 20)
# print(xerox)
# print(str(type(xerox)))
# scanner = Scanner.valid_constructor("Xerox-321", "red", "A1")
# print(scanner)
# printer = Printer.valid_constructor("HP34", "white", 4)
# print(printer)

commands = ("send", "take", "show", "q")
print("Добро пожаловать на склад!")
run = True
warehouse = Warehouse()
while run:
    print(f"\nДля работы используйте следующие команды меню:"
          f"\n{commands[0]:<8} - отправить на склад"
          f"\n{commands[1]:<8} - взять со склада"
          f"\n{commands[2]:<8} - показать склад"
          f"\n{commands[3]:<8} - выход")
    try:
        command = input("\nВведите команду: ")
        if command == "q" or command == "'q'":
            run = False
        elif command == "send" or command == "'send'":
            result = input_subcommands()
            if result is None:
                continue
            else:
                equipment = result[0]
                amount = result[1]
                warehouse.send_to_warehouse(equipment, amount)
        elif command == "take" or command == "'take'":
            result = input_subcommands()
            if result is None:
                continue
            else:
                equipment = result[0]
                amount = result[1]
                warehouse.take_from_warehouse(equipment, amount)
        elif command == "show" or command == "'show'":
            print(warehouse)
        else:
            print("Неизвестная команда. Попробуйте еще!")
    except MyIncorrectParameterError as err:
        print(f"Ошибка: {err}")
        print("Попробуйте еще!")
