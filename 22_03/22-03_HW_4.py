'''
4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
 Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
 Достаточно вернуть один допустимый вариант.
 *Верните все возможные варианты комплектации рюкзака.
'''
import random

goods = {
    "продукты": 5.0,
    "палатка": 3,
    "кружка": 0.2,
    "котелок": 0.5,
    "фонарик": 0.2,
    "ботинки": 0.8,
    "спички": 0.1,
    "топор": 1.5,
}

list_keys= []
for key in goods.keys():
    list_keys.append(key)

max_weight = 10.0
backpack = {}
weight_sum = 0

while len(list_keys) > 0:
    key_random = random.choice(list_keys)
    if weight_sum + goods[key_random] <= max_weight:
        backpack[key_random] = goods[key_random]
        weight_sum += goods[key_random]
    list_keys.remove(key_random)

print(f'В рюкзак влезли {backpack} массой {round(weight_sum, 1)}')
