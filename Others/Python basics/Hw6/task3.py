# Реализовать базовый класс Worker (работник).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


worker_one = Position("Ivan", "Ivanov", "CEO", 120000, 60000)

print(f"Name: {worker_one.name}")
print(f"Surname: {worker_one.surname}")
print(f"Position: {worker_one.position}")
print(f"Income_dict: {worker_one._income}")
print(f"Full_name: {worker_one.get_full_name()}")
print(f"Total_income: {worker_one.get_total_income()}\n")

worker_two = Position("John", "Smith", "Programmer", 60000, 40000)

print(f"Name: {worker_two.name}")
print(f"Surname: {worker_two.surname}")
print(f"Position: {worker_two.position}")
print(f"Income_dict: {worker_two._income}")
print(f"Full_name: {worker_two.get_full_name()}")
print(f"Total_income: {worker_two.get_total_income()}")
