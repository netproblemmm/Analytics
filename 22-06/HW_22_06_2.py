'''
2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''
from datetime import datetime as dt
from calendar import isleap
from sys import argv

__all__ = ['check_date']

def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        _isleap(t.year)
        return 'Дата валидна'
    except ValueError:
        return 'Дата неверна'


def _isleap(year: int):
    print('Високосный' if isleap(year) else 'Не високосный')


if __name__ == '__main__':
    if len(argv) == 2:
        print(check_date(argv[1]))
    print(check_date(input('Введите дату чч.мм.гггг: ')))