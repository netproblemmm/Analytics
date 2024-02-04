// Задайте двумерный массив символов (тип char [,]). Создать строку из символов этого массива.
using System;

char [,] chars = {{'a', 'b', 'c'}, {'d', 'e', 'f'}};
string res = GetStringFromCharArray(chars);
Console.WriteLine($"Result: {res}");

string GetStringFromCharArray (char[,] array)
{
    string result = string.Empty; // ""
    foreach (char symbol in array)
    {
        result += symbol;
    }
    return result;
}
