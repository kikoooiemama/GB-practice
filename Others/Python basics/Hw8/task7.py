# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return (f"{self.real}" if self.real != 0 else "") + \
               ("+" if self.imaginary > 0 else "") + \
               (f"{self.imaginary}j" if self.imaginary != 0 else "")

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + other.real * self.imaginary)


n = ComplexNumber(-1, 2)
print(n)
n = ComplexNumber(-1, 0)
print(n)
n = ComplexNumber(0, -5)
print(n)
# сложение
print("Сложение:")
n_1 = ComplexNumber(-3, 2)
n_2 = ComplexNumber(2, 4)
print(f"({n_1}) + ({n_2}) = {n_1 + n_2}")
# произведение
print("Произведение:")
n_1 = ComplexNumber(-3, 2)
n_2 = ComplexNumber(2, 4)
print(f"({n_1}) * ({n_2}) = {n_1 * n_2}")
