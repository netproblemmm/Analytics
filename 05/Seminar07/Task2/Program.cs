// Напишите программу, которая будет принимать на вход число и
// возвращать сумму его цифр

int SumOfDigits (int number)
{
// 63 = 3(63 % 10) + 6(6 % 10) + 0
if (number == 0) return 0; // 6 + 3 + 0 = 9
int result = number % 10 + SumOfDigits(number / 10);
return result;
// number = 35
// result = 5 + 3 + SumOfDigits(0) = 5 + 3 + 0
// SumOfDigits(3) = 3 + SumOfDigits(0)
}
Console.WriteLine(SumOfDigits(45));
