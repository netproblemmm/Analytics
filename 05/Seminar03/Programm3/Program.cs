// Найдите произведения пар чисел в одномерном массиве. Парой
// считаем первый и последний элемент, второй и предпоследний и
// т.д. Результат запишите в новый массив.
// Пример
// [1 3 2 4 2 3] => [3 6 8]
// [2 3 1 7 5 6 3] => [6 18 5] (элемент 7 не имеет пары)

int[] array = {11, 22, 33, 44, 55, 66, 77};
// Создаем массив на 3 элемента, причем [0, 0, 0]
int[] result = new int[array.Length / 2];

Console.WriteLine($"Массив: [ {string.Join(" | ", array)} ]");

for(int i = 0, j = array.Length - 1; i < result.Length; i++)
{
    result[i] = array[i] * array[j];
}

Console.WriteLine($"Результат: [ {string.Join(" | ", result)} ]");

if (array.Length % 2 == 1)
{
Console.Write($" (Число {array[array.Length / 2]} НЕ имеет пары)");
}
