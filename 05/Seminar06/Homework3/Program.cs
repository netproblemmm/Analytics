// Задайте произвольную строку. Выясните, является ли она палиндромом.
using System;

string str = string.Empty;
str = Console.ReadLine();

if (IsPalindrome(str))
{
    Console.WriteLine("Yes");
}
else
{
    Console.WriteLine("No");
}

bool IsPalindrome (string str)
{
    for (int i = 0; i < str.Length; i++)
    {
        Console.WriteLine(str[i]);
        if (str[i] != str[str.Length - 1 - i])
        {
            return false;
        }
    }
    return true;
}