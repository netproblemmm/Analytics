// Напишите программу, которая бесконечно запрашивает целые числа с консоли.
// Программа завершается при вводе символа ‘q’ или при вводе числа, сумма цифр которого чётная.

while(true)
{
    Console.Write("Введите текст: ");
    string text = Console.ReadLine();
    if (text == "q")
    {
        break;
    }

    // Проверка, что строчка состоит только из цифр
    int number; // введенное число (или 0, если в строчке есть символы)
    
    if (int.TryParse(text, out number))
    {
        Console.WriteLine("Введенная строчка состоит из цифр");
        int sum = 0;

        while (number > 0)
        {
            sum += number % 10;
            number /= 10; // Избавляемся от последней цифры
        }

        if (sum % 2 == 0)
        {
            Console.WriteLine("Сумма цифр - четная");
            break;
        }
    }
    else
    {
        Console.WriteLine("В введенной строчке есть НЕ цифры");
    }
}