# Запись в файл
# colors = ['red', 'green', 'blue']
# data = open('./01-10/file.txt', 'a') # a - append (добавление данных в файл)
# data.writelines(colors) # разделителей не будет
# data.close()

# Чтобы файл закрывался автоматом - используем with:
with open('./01-10/file.txt', 'w') as data: # w - режим перезаписи файла
    data.write('line 1\n')
    data.write('line 2\n')
