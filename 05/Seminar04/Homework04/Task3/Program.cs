// Напишите программу, которая перевернёт одномерный массив (первый элемент станет последним, второй – предпоследним и т.д.)

int size = 10;
int[] array1 = new int[size]; // Массив array на size элементов
for (int i = 0; i < size; i++)
{
    array1[i] = new Random().Next(1, 10);
    // 100,1000: 100-999
}

int[] array2 = new int[size]; // Массив array на size элементов

for (int i = 0; i < size; i++)
{
    array2[size - 1 - i] = array1[i];
}

Console.WriteLine($"Массив: [ {string.Join("; ", array1)} ]");
Console.WriteLine($"Массив: [ {string.Join("; ", array2)} ]");