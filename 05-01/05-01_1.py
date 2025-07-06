# Lesson_01: Task_01
# 1.1

dict1 = {1: "q", 2: "w"}
dict2 = {3: "a", 4: "d"}
dict1.update(dict2)
print(dict1)

# 1.2 using function
dict1 = {1: "q", 2: "w"}
dict2 = {3: "a", 4: "d"}
def merge_dict(dict1: dict, dict2: dict) -> dict:
    dict1.update(dict2)
    return dict1

print(merge_dict(dict1, dict2))