# Задание 1: Видеокарты
GPU_list = ['3070', '2060', '3090', '3070', '3090']
GPU_new_list = []
max_item = 0

for i in GPU_list:
    if int(i) > max_item:
        max_item = int(i)

for i in GPU_list:
    if int(i) != max_item:
        GPU_new_list.append(i)

print('Старый список видеокарт: ', GPU_list)
print('Удаленная модель:', max_item)
print('Новый список видеокарт: ', GPU_new_list)