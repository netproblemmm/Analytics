string GetLettersFromString(string s)
{
    string letters = "";
    foreach(char e in s)
    {
        if (char.IsAsciiLetter(e))
        {
            letters += e;
        }
    }
    return letters;
}

string str = Console.ReadLine();
string result = GetLettersFromString(str);
Console.WriteLine(result);