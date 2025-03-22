# Задача 4. Гистограмма частоты
# Функция для создания словаря частот символов
def histogram(string):
    # Инициализируем пустой словарь для частот
    sym_dict = dict()
    
    for sym in string:
        # Если символ уже есть в словаре, увеличиваем его частоту
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
        # Если символа нет в словаре, добавляем его с частотой 1
            sym_dict[sym] = 1
    return sym_dict

# Функция для инвертирования словаря частот
def invert_dict(d):
    # Инициализируем пустой словарь для инвертированных данных
    inv = dict()

    for key in d:
        val = d[key]
        # Если частота еще не встречалась, создаем новый список
        if val not in inv:
            inv[val] = [key]
        else:
        # Если частота уже есть в словаре, добавляем символ в существующий список
            inv[val].append(key)
    return inv

# Запрашиваем текст у пользователя
text = input('Введите текст: ')
# Создаем словарь частот
hist = histogram(text)

# Выводим оригинальный словарь частот
print('Оригинальный словарь частот:')
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

# Создаем инвертированный словарь частот
inv_hist = invert_dict(hist)
# Выводим инвертированный словарь частот
print('\n Инвертированный словарь частот:')
for i_sym in sorted(inv_hist.keys()):
    print(i_sym, ':', inv_hist[i_sym])