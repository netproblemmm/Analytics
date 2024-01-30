using System;

//Тело класса будет написано студентом. Класс обязан иметь статический метод PrintResult()
class UserInputToCompileForTest
{
    /// Вычисление сумм по строкам (на выходе массив с суммами строк)
    public static int[] SumRows(int[,] array)
    {
        int rowsQty = array.GetLength(0);
        int columnsQty = array.GetLength(1);

        int[] sums = new int[rowsQty];
        for(int i = 0; i < rowsQty; i++)
        {
            int sumOfNumbersFromRow = 0;
            for(int j = 0; j < columnsQty; j++)
            {
                sumOfNumbersFromRow += array[i, j];
            }
            sums[i] = sumOfNumbersFromRow;
            Console.WriteLine($"Сумма цифр в строке {i} - {sumOfNumbersFromRow}");
        }
        return sums;
    }
    
    // Получение индекса минимального элемента в одномерном массиве
    public static int MinIndex(int[] array)
    {
        int index = 0;
        int min = array[0];
        for(int i = 0; i < array.GetLength(0); i++)
        {
            if (array[i] < min)
            {
                min = array[i];
                index = i;
            }
        }
        return index + 1;
    }
    public static void PrintResult(int[,] numbers)
    {
        int rowsQty = numbers.GetLength(0);
        int columnsQty = numbers.GetLength(1);
        for (int i = 0; i < numbers.GetLength(0); i++) //  стр 
        {
            for (int j = 0; j < numbers.GetLength(1); j++)// столб
            {
                Console.Write($"{numbers[i, j]}\t"); // \t = 4 пробела
            }
            Console.WriteLine();
        }
        Console.WriteLine();

        int[] sums = SumRows(numbers);
        int indexOfMinimal = MinIndex(sums);
        Console.WriteLine($"Строка с наименьшей суммой - {indexOfMinimal}");
    }
}

//Не удаляйте и не меняйте класс Answer!
class Answer
{
    public static void Main(string[] args)
    {
        int[,] numbers;

        if (args.Length >= 1)
        {
            // Предполагается, что строки разделены запятой и пробелом, а элементы внутри строк разделены пробелом
            string[] rows = args[0].Split(',');

            int rowCount = rows.Length;
            int colCount = rows[0].Trim().Split(' ').Length;

            numbers = new int[rowCount, colCount];

            for (int i = 0; i < rowCount; i++)
            {
                string[] rowElements = rows[i].Trim().Split(' ');

                for (int j = 0; j < colCount; j++)
                {
                    if (int.TryParse(rowElements[j], out int result))
                    {
                        numbers[i, j] = result;
                    }
                    else
                    {
                        Console.WriteLine($"Error parsing element {rowElements[j]} to an integer.");
                        return;
                    }
                }
            }
        }
        else
        {
            // Если аргументов на входе нет, используем примерный массив
            numbers = new int[,]
            {
                {1, 2, 3},
                {1, 1, 0},
                {7, 8, 2},
                {9, 10, 11}
            };      
        }
        UserInputToCompileForTest.PrintResult(numbers);
    }
}