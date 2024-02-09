// Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N.
// Использовать рекурсию, не использовать циклы.

Console.Write("Введите начальное число: ");
int m = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите конечное число: ");
int n = Convert.ToInt32(Console.ReadLine());

void ShowNumbers(int start, int end)
{
    if (start == end)
    {
        Console.Write(start);
        return; // Ломает всю программу, если попали в этот фрагмент
    }
    Console.Write(start + " ");
    ShowNumbers(start + 1, end);
}

ShowNumbers(m, n); // start = m, end = n
