using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace atmBanksystem
{
    public class bankAccount
    {
        public static void log(string message, string level = "info")
        {
            string time = DateTime.Now.ToString("h:mm:ss tt");
            using (StreamWriter file = new StreamWriter(Directory.GetCurrentDirectory() + "/log.txt", append: true))
            {
                file.WriteLine($"{level}:{time}:{message}");
            };


        }
        private double balance;
        private string currency;

        public double deposit(double amount)
        {
            this.balance += amount;
            Console.WriteLine($"Deposited {this.currency}{amount} to account");
            log($"Deposited {amount}");
            return amount;
        }
        public double withdraw(double amount)
        {
            if (amount < 0) { amount *= -1; }
            if (this.balance >= amount)
            {
                this.balance -= amount;
                Console.WriteLine($"Withdrew {this.currency}{amount} from account");
                log($"Withdrew {amount}");
                return amount;
            }
            else
            {
                Console.WriteLine("ERROR: You do not have that much money!");
                Console.WriteLine($"You have {this.currency}{this.balance}");
                log("User tried to withdraw too much money!", level:"warning");
                return amount;
            }
        }

        public void checkBalance()
        {
            Console.Write(this.balance);
            Console.WriteLine(this.currency);
            log("Checked balance");
        }
        public bankAccount(double startingBalance = 0, string currency="kr.")
        {
            this.balance = startingBalance;
            this.currency = currency;
        }
    }
}
