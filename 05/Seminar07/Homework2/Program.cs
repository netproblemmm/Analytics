// Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.

Console.Write("Введите начальное число: ");
int n = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите конечное число: ");
int m = Convert.ToInt32(Console.ReadLine());

int AkkermanFoo(int n, int m)
{
    while (n != 0)
    {
        if (m == 0)
        {
            m = 1;
        }
        else
        {
            m = AkkermanFoo(n, m - 1);
        }
        n -= 1;
    }
    return (m + 1);
}

Console.Write(AkkermanFoo(n, m));
