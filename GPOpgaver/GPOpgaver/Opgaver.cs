using System;
using System.Collections.Generic;
using System.Text;

namespace GPOpgaver
{
    public static class Opgaver
    {
        /*
        * Introduktion til Algoritmer
        * Exercise 1. 
        * Describe an algorithm that interchanges the values of the variables x and y, using only assignment statements.
        * What is the minimum number of assignment statements needed to do so?
        */
        public static void Interchange(ref int x, ref int y)
        {
            int z = x;
            x = y;
            y = z;
            //Write your solution here
        }
        /*
        * Introduktion til Algoritmer
        * Exercise 2. 
        * 2.Describe an algorithm that uses only assignment statements to replace thevalues of the triple(x, y, z) with (z, x, y).
        * What is the minimum number of assignment statements needed?
        */
        public static void InterchangeTriple(ref int a, ref int b, ref int c)
        {
            //Write your solution here
            int z = a;
            a = c;
            c = b;
            b = z;
        }
        /*
         * Introduktion til Algoritmer
         * Exercise 3.
         * A palindrome is a string that reads the same forward and backward.
         * Describe an algorithm for determining whether a string of n characters is a palindrome.
         */
        public static bool IsPalindrome(string s)
        {
            char[] sA = s.ToCharArray();
            char[] reversed = new char[sA.Length];
            char[] temp = s.ToCharArray();
            for(int i = sA.Length; i>0; i--)
            {
                reversed[sA.Length-i] = temp[i-1];
            }
            string reversedS = new string(reversed);
            return reversedS == s;
            
            //Write your solution here
        }
        /*
         * Introduktion til Algoritmer
         * Exercise 4.a.
         * List all the steps used to search for 9 in the sequence 1, 3, 4, 5, 6, 8, 9, 11
         * Do this by completing the unit test for 4A
         */
        public static int StepsInLinearSearch(int searchFor, int[] intergerArray)
        {
            int count = 0;
            foreach (int i in intergerArray)
            {
                count++;
                if (i == searchFor)
                {
                    break;
                }
            }
            return count;
            //Write your solution here
        }
        /*
         * Introduktion til Algoritmer
         * Exercise 4.b.
         * List all the steps used to search for 9 in the sequence 1, 3, 4, 5, 6, 8, 9, 11
         * Do this by completing the unit test for 4B
         */
        public static int StepsInBinarySearch(int[] integerArray, int arrayStart, int arrayEnd, int searchFor)
        {
            int count = 0;
            while (arrayStart <= arrayEnd)
            {
                int arrayMid = arrayStart + (arrayStart + arrayEnd) / 2;
                if (searchFor == integerArray[arrayMid])
                {
                    count++;
                    break;
                }
                else if (searchFor < integerArray[arrayMid])
                {
                    arrayEnd = arrayMid - 1;
                    count++;
                }
                else if (searchFor > integerArray[arrayMid])
                {
                    arrayEnd = arrayMid + 1;
                    count++;
                }
            }
            return count;
            //Write your solution here
        }
        /*
         * Introduktion til Algoritmer
         * Exercise 5.
         * Describe an algorithm based on the linear search for de-termining the correct position in which to insert a new element in an already sorted list.
         */
        public static int InsertSortedList(List<int> sortedList, int insert)
        {
            for(int i = 0; i<sortedList.Count; i++)
            {
                if (sortedList[i] < insert && sortedList[i+1] > insert)
                {
                    return ++i;
                }
            }
            return 0;
            //Write your solution here
        }
        /*
         * Exercise 6.
         * Arrays
         * Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num up to length.
         * Notice that num is also included in the returned array.
         */
        public static int[] ArrayOfMultiples(int num, int length)
        {
            int[] nums = new int[length];
            for (int i = 0; i<=length; i++)
            {
                nums[i] = num * i;
            }
            return nums;
            //Write your solution here
        }
        /*
         * Exercise 7.
         * Create a function that takes in n, a, b and returns the number of values raised to the nth power that lie in the range [a, b], inclusive.
         * Remember that the range is inclusive. a < b will always be true.
         */
        public static int PowerRanger(int power, int min, int max)
        {
            int counter = 0;
            for (int i = min; i <= max; i++)
            {
                if (Math.Pow(i, 1.0 / power) % 1 == 0) counter++;
            }
            return counter;
            //Write your solution here
        }
        /*
         * Exercise 8.
         * Create a Fact method that receives a non-negative integer and returns the factorial of that number.
         * Consider that 0! = 1.
         * You should return a long data type number.
         * https://www.mathsisfun.com/numbers/factorial.html
         */
        public static long Factorial(int n)
        {
            if (n == 1)
            {
                return 1;
            }
            else
            {
                return n * Factorial(n - 1);
            }
            //Write your solution here
        }
        /*
         * Exercise 9.
         * Write a function which increments a string to create a new string.
         * If the string ends with a number, the number should be incremented by 1.
         * If the string doesn't end with a number, 1 should be added to the new string.
         * If the number has leading zeros, the amount of digits should be considered.
         */
        public static string IncrementString(string txt)
        {

            throw new NotImplementedException();
        }
        /*
         * Exercise 10.
         * Write a more effectiv version of this function.
         */
    }
}