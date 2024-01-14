// Задайте массив. Напишите программу, которая определяет,
// присутствует ли заданное число в массиве. Программа
// должна выдать ответ: Да/Нет.
// Примеры
// [1 3 4 19 3], 8 => Нет
// [-4 3 4 1], 3 => Да

int[] array = {11, 22, 33, 44, 55};
Console.Write("Введите число для поиска: ");
int numberForSearch = Convert.ToInt32(Console.ReadLine());
bool isFound = false;

for(int i = 0; i < array.Length; i++)
{
    if(numberForSearch == array[i])
    {
        isFound = true;
        break;
    }
}

if(isFound)
{
    Console.Write("да");
}
else
{
    Console.Write("нет");
}
