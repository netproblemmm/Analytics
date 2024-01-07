Console.WriteLine("Введите число: ");
string str = Convert.ToString(Console.ReadLine());

int i = 0;
while (i <= str.Length - 1)
{
    if (i < str.Length - 1)
    {
        Console.Write(str[i] + ", ");
    }
    else
    {
        Console.Write(str[i]);
    }

    i += 1;
}
