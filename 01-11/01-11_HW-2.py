# Задача 2. Zip
from typing import List, Tuple

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# list_new = [letters[i] + int(numbers[i]) for i in range(min(len(letters), len(numbers)))] # не работает

list_new: List[Tuple[str, int]] = list(map(lambda x, y: (x, y), letters, numbers))
print(list_new)