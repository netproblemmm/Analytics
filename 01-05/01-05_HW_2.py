# Задача 2. Кино
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
my_films = []

films_qty = int(input('Сколько фильмов хотите добавить? '))
for i in range(films_qty):
    film_name = input('Введите название фильма: ')
    if films.__contains__(film_name):
        my_films.append(film_name)
    else:
        print(f'Ошибка: фильма {film_name} у нас нет')

print(*films, sep =', ') # вывести весь массив через запятую
print('Ваш список любимых фильмов: ')
print(*my_films, sep =', ')
