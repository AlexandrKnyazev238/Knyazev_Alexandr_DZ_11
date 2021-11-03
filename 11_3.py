# Task_3

class MyErr(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


list_1 = []
while True:
    a = input('Введите число. Чтобы прекратить ввод: "stop": ')
    if a == 'stop':
        print(list_1)
        break
    else:
        try:
            if not a.isdigit():
                raise MyErr(f'Элемент списка {a} не является числом')
        except ValueError:
            print()
        except MyErr as terr:
            print(terr)
        else:
            list_1.append(a)
