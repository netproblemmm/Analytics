// Напишите программу, которая принимает на вход число и
// возвращает 3 цифру с начала введенного числа
// Примеры:
// 12345678 => 3
// 78671 => 6

Console.Write("Введите число: ");
int number = Convert.ToInt32(Console.ReadLine());

if(number > 99)
{
    int copyNumber = number;
    
    while(copyNumber > 999)
    {
        copyNumber /=10;
    }
    int result = (copyNumber % 10);

    Console.WriteLine($"Результат: {number} => {result}");
}
else
{
    Console.WriteLine("Число не трехзначное или отрицательное");
}
