Console.WriteLine("Введите число: ");
int N = Convert.ToInt32(Console.ReadLine());
int negativeN = -N;

while(negativeN <= N)
{
    Console.Write(negativeN + "\t");
    negativeN++;
}
