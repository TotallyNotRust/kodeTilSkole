using System;
using System.Text.Json;
using System.IO;
using System.Threading.Tasks;

namespace atmBanksystem
{
    class Program
    {

        static void Main(string[] args)
        {
            bankAccount account = new bankAccount(); 
            while (true)
            {
                doBankStuff(account);
            }
        }
        static void doBankStuff(bankAccount account) 
        { 
            Console.WriteLine("########################");
            Console.WriteLine("# [D]: Deposit         #");
            Console.WriteLine("# [W]: Withdraw        #");
            Console.WriteLine("# [C]: Check balance   #");
            Console.WriteLine("########################");
            ConsoleKey key = Console.ReadKey(true).Key;
            switch (key)
            {
                case ConsoleKey.D:
                    while (true) {
                        try
                        {
                            Console.Write("How much to deposit: ");
                            double amount = account.deposit(Convert.ToDouble(Console.ReadLine()));
                            break;
                        }
                        catch 
                        {
                            Console.WriteLine("Not valid input; use [0.0]");
                        }
                        
                    }
                    break;
                case ConsoleKey.W:
                    while (true)
                    {
                        try
                        {
                            Console.Write("How much to withdraw: ");
                            double amount = account.withdraw(Convert.ToDouble(Console.ReadLine()));
                            break;
                        }
                        catch
                        {
                            Console.WriteLine("Not valid input; use [0.0]");
                        }
                    }
                    break;
                case ConsoleKey.C:
                    account.checkBalance();
                    break;
            }
        }
    }
}
