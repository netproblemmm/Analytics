Console.WriteLine("Введите число X: ");
int x = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число Y: ");
int y = Convert.ToInt32(Console.ReadLine());
int coordNumber = 0;

if (x > 0 && y > 0)
{
    coordNumber = 1;
}
if (x < 0 && y > 0)
{
    coordNumber = 2;
}
if (x < 0 && y < 0)
{
    coordNumber = 3;
}
if (x > 0 && y < 0)
{
    coordNumber = 4;
}

Console.WriteLine("Номер координатной четверти = " + coordNumber);

