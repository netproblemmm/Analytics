# Задача 3. Палиндром
from collections import Counter

def can_be_poly(val: str) -> bool:
    char_counts = Counter(val)
    odd_count = len(list(filter(lambda x: x % 2, char_counts.values())))

    return odd_count < 2

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))