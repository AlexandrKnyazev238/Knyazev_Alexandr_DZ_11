# Task_1

class Date:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def valid(d, m, y):
        if 0 < d < 32 and 0 < m < 13 and 2000 < y < 2022:
            print(f'{d}-{m}-{y} Корректная дата!')
        else:
            print(f'Некорректные данные: {d}-{m}-{y}!')

    @classmethod
    def new_date(cls, date):
        true_date_list = []
        date_list = date.split('-')
        for i in date_list:
            if i.isdigit():
                true_date_list.append(i)
            else:
                print(f'Некорректные данные: {date}!')
                return 0
        a, b, c = map(int, true_date_list)
        return Date.valid(a, b, c)


Date.new_date('19-01-1995')
Date.new_date('u8-08-2021')
Date.new_date('28-03-2021')
