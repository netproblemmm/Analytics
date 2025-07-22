'''
2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
 Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
'''

import os
import json
import csv
import pickle


def directory_tree(directory):
    directory_list = []

    for root, dirs, files in os.walk(directory):
        dir_size = 0

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            dir_size += file_size
            directory_list.append({'path': file_path, 'type': 'file', 'size': file_size, 'parent_dir': root})
        
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size += get_dir_size(dir_path)
            directory_list.append({'path': dir_path, 'type': 'directory', 'size': dir_size, 'parent_dir': root})

        save_json(directory_list, 'result.json')
        save_csv(directory_list, 'result.csv')
        save_pickle(directory_list, 'result.pickle')


def get_dir_size(path):
    total_size = 0

    for path, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(path, file)
            total_size += os.path.getsize(file_path)

    return total_size


def save_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def save_csv(data, filename):
    header = ['path', 'type', 'size', 'parent_dir']
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


def save_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


if __name__ == '__main__':
    directory_tree('d:/Projects/Analytics/22_08/HW_8/test_dir_1')
