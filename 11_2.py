# Task_2

class MyError(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


num_1 = input('Введите делимое: ')
num_2 = input('Введите делитель: ')
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_2 == 0:
        raise MyError('Делитель равен нулю.')
except MyError as nr:
    print(nr)
except ZeroDivisionError:
    print()
else:
    print(num_1 / num_2)
