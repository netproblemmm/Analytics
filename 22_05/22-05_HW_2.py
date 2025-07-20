'''
2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
 Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''
def file_path(text: str):
    """Функция возвращает кортеж из трёх элементов: путь, имя файла
      расширение файла.
    """

    *_, file = text.split('/')
    *_, extension = file.split('.')
    file_name = file[:-(len(extension) + 1)]
    file_path = text[:-(len(file) + 1)]
    return file_path, file_name, extension


if __name__ == '__main__':
    text_1 = "d:/Gb/python/22-05/22-05_HW_2.py"
    text_2 = "https://apod.nasa.gov/apod/fap/image/2304/TSE2023-Comp48-2a1024.jpg"
    print(file_path(text_1))
    print(file_path(text_2))