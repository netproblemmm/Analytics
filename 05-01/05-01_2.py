# Lesson_01: Task_02
# 2.1 Using FOR

list1 = ["one", "two", "three"]
list2 = [1, 2, 3]

def get_dict(keys: list, values: list) -> dict:
    dict1 = {}

    for i in range(len(keys)):
        dict1.update({keys[i]: values[i]})

    return dict1
    
print(get_dict(list1, list2))

# 2.2 Using dict comprehensions

def get_dict_c(keys: list, values: list) -> dict:
    return {keys[i]: values[i] for i in range(len(keys))}

print(get_dict_c(list1, list2))