# Функция zip, 'сшивает' вместе значения из разных массивов
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)
# результат будет равен = [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# при сшивании берется минимальный набор данных (если в salary 3 значения, то берется только 3)
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)
# результат будет равен = [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]
