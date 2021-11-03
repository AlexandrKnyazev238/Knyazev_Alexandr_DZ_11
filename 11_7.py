# Task_7

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма равна: ')
        return f'{self.a + other.a} | {self.b + other.b}'

    def __mul__(self, other):
        print(f'Произведение равно: ')
        return f'{self.a * other.a} | {self.b * other.b}'


val_1 = Complex(23, 7)
val_2 = Complex(8, 77)
print(val_1 + val_2)
print(val_1 * val_2)
