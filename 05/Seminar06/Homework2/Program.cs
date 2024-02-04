// Задайте строку, содержащую латинские буквы в обоих регистрах.
// Сформируйте строку, в которой все заглавные буквы заменены на строчные. 
// "aBcDefG" -> "abcdefg"
using System;

string str = "aBcDefG";
Console.WriteLine(GetStringToLower(str));

string GetStringToLower(string str)
{
    str = str.ToLower();
    return str;
}
