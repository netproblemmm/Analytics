# Lesson_01: Task_03
# 3.1 Using FOR

client_dict = {
    'name': 'John',
    'age': 25,
    'salary': 5000,
    'city': 'Moscow'
}

def get_dict(base_d: dict, keys: list = ['name', 'age']) -> dict:
    res = dict()

    for i in keys:
        res.update({i: base_d[i]})

    return res
    
print(get_dict(client_dict))
print(get_dict(client_dict, ['salary']))

# 3.2 Using dict comprehensions

def get_dict_c(base_d: dict, keys: list = ['name', 'age']) -> dict:
    return {i: base_d[i] for i in keys}

print(get_dict_c(client_dict))
print(get_dict_c(client_dict, ['salary']))