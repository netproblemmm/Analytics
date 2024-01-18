﻿// Задайте массив из 10 элементов, заполненный числами из
// промежутка [-10, 10]. Замените отрицательные элементы на
// положительные, а положительные на отрицательные.
// Пример
// [1 -5 6]
// => [-1 5 -6]

int[] array = {-2, -1, -3, -4, -5, 0, 1, 8, 7, 3};
Console.WriteLine($"Массив ДО: [ {string.Join(" | ", array)} ]");

for(int i = 0; i < array.Length; i++)
{
    array[i] *= -1;
}

Console.WriteLine($"Массив ПОСЛЕ: [ {string.Join(" | ", array)} ]");