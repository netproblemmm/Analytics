// Напишите программу, которая принимает на вход число и
// выводит 3 цифру с конца или сообщает, что третьей цифры нет
// Примеры:
// 456 => 4
// 7812 => 8
// 91 => третьей цифры нет

Console.Write("Введите число: ");
int number = Convert.ToInt32(Console.ReadLine());

if(number > 99)
{
    int result = (number / 100 % 10);
    Console.WriteLine($"Третья цифра справа {number} => {result}");
}
else
{
    Console.WriteLine("Третьей цифры нет или число отрицательное");
}
