using System;
using Xunit;
using System.Collections.Generic;
using GPOpgaver;

namespace XUnitTestGPOpgaver
{
    public class AlgoritmerIntroTest
    {
        [Fact]
        public void Exercise1Test()
        {
            int x = 5, y = 10;
            Opgaver.Interchange(ref x, ref y);
            Assert.Equal(10, x);
            Assert.Equal(5, y);
        }
        [Fact]
        public void Exercise2Test()
        {
            int a = 1, b = 2, c = 3;
            Opgaver.InterchangeTriple(ref a, ref b, ref c);
            Assert.Equal( 3, a);
            Assert.Equal( 1, b);
            Assert.Equal( 2, c);
        }

        [Fact]
        public void Exercise3Test()
        {
            string palindrome = "level";
            Assert.True(Opgaver.IsPalindrome(palindrome));
            palindrome = "cammac";
            Assert.True(Opgaver.IsPalindrome(palindrome));
            palindrome = "kayak";
            Assert.True(Opgaver.IsPalindrome(palindrome));
            palindrome = "ward draw";
            Assert.True(Opgaver.IsPalindrome(palindrome));
        }
        [Fact]
        public void Exercise4ATest()
        {
            int[] intArray = { 1, 3, 4, 5, 6, 8, 9, 11 };
            Assert.Equal( 8, Opgaver.StepsInLinearSearch(11, intArray));
            Assert.Equal( 4, Opgaver.StepsInLinearSearch(5, intArray));
            //Assert.Equal(???, Opgaver.StepsInLinearSearch(9, intArray));
        }
        [Fact]
        public void Exercise4BTest()
        {
            int[] intArray = { 1, 3, 4, 5, 6, 8, 9, 11 };
            Assert.Equal( 2, Opgaver.StepsInBinarySearch(intArray, 0, intArray.Length - 1, 3));
            Assert.Equal( 1, Opgaver.StepsInBinarySearch(intArray, 0, intArray.Length - 1, 5));
            //Assert.Equal(???, Opgaver.StepsInBinarySearch(intArray, 0, intArray.Length - 1, 9));
        }
        [Fact]
        public void Exercise5Test()
        {
            List<int> lista = new List<int>{ 1, 2, 3, 5, 6, 8, 9};
            Assert.Equal( 3, Opgaver.InsertSortedList(lista, 4));
            List<int> listb = new List<int> { 1, 2, 3, 5, 6, 8, 9 };
            Assert.Equal( 5, Opgaver.InsertSortedList(listb, 7));
        }
    }
}
