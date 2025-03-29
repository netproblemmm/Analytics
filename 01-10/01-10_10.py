# Чтение из файла
path = './01-10/file.txt'
data = open(path, 'r') # r - read (чтение данных из файла)

for line in data:
    print(line)
    
data.close()
