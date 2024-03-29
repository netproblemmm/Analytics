﻿// Рекурсия - метод, который вызывается внутри метода

// Факториал - произведение чисел от 1 до n включительно
// 4! = 4 * 3 * 2 * 1
// n -> 1

int FindFactorial (int n)
{
// Базовый случай - случай выхода из рекурсии
if (n == 1) return 1;
if (n == 0) return 1; // Факториал от нуля равен 1
// 4 * 3 * 2 * x(1)
// Рекурсивный случай - тут и происходит вызов метода внутри метода
return n * FindFactorial(n - 1);
}

Console.WriteLine(FindFactorial(4)); // 4 * 3 * 2 * Find(1)
