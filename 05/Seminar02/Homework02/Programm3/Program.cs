int number = 0;
while (number < 10 || number > 99)
{
    Console.WriteLine("Введите число от 10 до 99: ");
    number = Convert.ToInt32(Console.ReadLine());
}
int firstNumber = number / 10;
int secondNumber = number % 10;

if (firstNumber > secondNumber)
{
    Console.WriteLine("Наибольшая цифра числа = " + firstNumber);
}
else
{
    Console.WriteLine("Наибольшая цифра числа = " + secondNumber);
}
