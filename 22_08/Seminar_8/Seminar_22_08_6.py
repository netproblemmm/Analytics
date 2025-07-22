'''
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
 Для тестированию возьмите pickle версию файла из задачи 4 семинара.
   Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
'''

import csv
import pickle
from pathlib import Path


def pickle2csv(file: Path) -> None:
    with (
        open(file, 'rb') as f_read,
        open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f_write,
    ):
        data = pickle.load(f_read)
        keys = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=keys, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    pickle2csv(Path('new_users.pickle'))
