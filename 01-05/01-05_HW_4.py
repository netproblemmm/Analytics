# Задача 4. Товары
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for item_name in goods.keys():
    item_code = goods[item_name]
    total_qty = 0
    total_sum = 0
    for entry in store[item_code]:
        total_qty += entry['quantity']
        total_sum += entry['quantity'] * entry['price']
    print ('{} - {} штук, стоимость {} рубля(ей).'.format(item_name, total_qty, total_sum))

