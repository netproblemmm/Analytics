Console.WriteLine("Введите 1 число: ");
int firstNumber = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Введите 2 число: ");
int secondNumber = Convert.ToInt32(Console.ReadLine());

if (firstNumber == secondNumber * secondNumber)
{
    Console.WriteLine("Да, " + firstNumber + " является квадратом от " + secondNumber);
}
else
{
    Console.WriteLine("Нет, " + firstNumber + " не является квадратом от " + secondNumber);
}
