# Lesson_01: HW_2

products = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']

def unique_products_count(list) -> int:
    return len(set(list))

print(unique_products_count(products))