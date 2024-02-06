﻿// Считать строку с консоли, содержащую латинские буквы.
// Вывести на экран согласные буквы этой строки.
// Использовать рекурсию. Не использовать цикл.
// Пример:
// “hello” => h l l
// “World” => W r l d
// “Hello world!” => H l l w r l d

ShowConsonant("4!3CAT");

void ShowConsonant (string str)
{
    // Базовый случай
    if (str.Length == 0)
    {
        return;
    }
    string vowels = "aoueyi"; // Гласные буквы

    // CAT -> c
    if (char.IsAsciiLetter(str[0]) && !vowels.Contains(char.ToLower(str[0])))
    {
        Console.Write(str[0] + " ");
    }
    
    // Рекурсивный случай
    // CAT -> AT -> T
    ShowConsonant(str.Substring(1));
}
