// Задайте массив заполненный случайными трёхзначными числами.
// Напишите программу, которая покажет количество чётных чисел в массиве.

int size = 10;
int[] array = new int[size]; // Массив array на size элементов
for (int i = 0; i < array.Length; i++)
{
    array[i] = new Random().Next(100, 1000);
    // 100,1000: 100-999
}

int evenNumberQuantity = 0;
foreach (int e in array)
{
    if (e % 2 == 0)
    evenNumberQuantity += 1;
}

Console.WriteLine($"Массив: [ {string.Join("; ", array)} ]");
Console.WriteLine($"Количество четных номеров: {evenNumberQuantity}");