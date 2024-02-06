﻿// Задайте значение N. Напишите программу, которая выведет
// все натуральные числа в промежутке от 1 до N.
// Использовать рекурсию. Не использовать цикл.
// Пример:
// N = 5 => 1 2 3 4 5

Console.Write("Введите число: ");
int N = Convert.ToInt32(Console.ReadLine());
int start = 1;
// start = 1, end = 5

void ShowNumbers(int start, int end)
{
    if (start == end)
    {
        Console.Write(start);
        return; // Ломает всю программу, если попали в этот фрагмент
    }
    Console.Write(start + " "); // 1 2 3 4 5
    ShowNumbers(start + 1, end);
}

ShowNumbers(1, N); // start = 1, end = N
