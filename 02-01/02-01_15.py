# Файл содержит данные о продажах товаров: Наименование товара и Количество проданных единиц
# Напишите программу, которая открывает текстовый файл salex.txt,
# читает его содержимое и выводит общее количество проданных единиц для каждого товара.
import os
os.chdir('D:/Projects/Analytics/02-01') 

def analyze_sales(filename: str) -> dict: # typing, необязателен, программа его игнорирует, просто для информации - что возвращает функция
    sales_data = {}

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            product, quantity = line.split('-')
            quantity = int(quantity)

            if product in sales_data.keys():
                sales_data[product] += quantity
            else:
                sales_data[product] = quantity

    for product, quantity in sales_data.items():
        print(f'{product}: {quantity}')

analyze_sales('02-01_15_sales.txt')