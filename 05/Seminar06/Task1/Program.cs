// Задайте массив символов (тип char []). Создайте строку из
// символов этого массива.
// [‘a’, ‘b’, ‘c’, ‘d’] => “abcd”

string GetStringFromCharArray (char[] array)
{
    string result = string.Empty; // ""
    foreach (char symbol in array)
    {
        result += symbol;
    }
    return result;
}

char[] chars = {'1', 'd', '!', '2', 'f'};
string res = GetStringFromCharArray(chars);
Console.WriteLine($"Result: {res}");
