# Задача 5. Пицца
raw_orders = ['Иванов Пепперони 1', 'Петров Де-Люкс 2', 'Иванов Мясная 3', 'Иванов Мексиканская 2', 'Иванов Пепперони 2', 'Петров Интересная 5']

database = dict()

print('Заказы')

for order in range(len(raw_orders)):
    customer, pizza_name, qty = raw_orders[order].split()
    qty = int(qty)
    print (customer, pizza_name, qty)
    if customer not in database:
        database[customer] = {pizza_name: qty}
    else:
        if pizza_name in database[customer]:
            database[customer] [pizza_name] += qty
        else:
            database[customer] [pizza_name] = qty

print()
print('Покупатели')

for customer in sorted(database.keys()):
    print('{}:'.format(customer))

    for pizza_name in sorted(database[customer].keys()):
        print('{}: {}'.format(pizza_name, database[customer] [pizza_name]))
