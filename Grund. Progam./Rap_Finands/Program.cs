using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;

namespace Rap_Finands
{
    /**
    Dette BANK PROGRAM ER LAVET af Konrad Sommer! Copy(c) Right All rights reserveret 2020
    idé og udtænkt af Anne Dam for Voldum Bank I/S
    Rap Finands
    **/
    class Program
    {
        public static string reginummer = "4242";
        public static string datafil = "bank.json"; //Her ligger alt data i
        public static List<Konto> konti;
        // Fjernet belob da den kun blev brugt til en fejl..
        static void Main(string[] args)
        {
            Console.WriteLine("Henter alt kontodata");
            
            Hent();
            if (konti.Count == 0) {
                var k = LavKonto();
                k.ejer = "Ejvind Møller";
                konti.Add(k);

                GemTrans(k,"Opsparing",100);
                GemTrans(konti[0],"Vandt i klasselotteriet",1000);
                GemTrans(konti[0],"Hævet til Petuniaer",-50);
                
                Gem();
            } // Tom else 
            DosStart();
            
        }
        static void DosStart() {
            Console.WriteLine("Velkommen til Rap Finans af Konrad Sommer");
            Console.WriteLine("Hvad vil du gøre nu?");
            
            bool blivVedOgVed = true;
            while (blivVedOgVed) {
                Console.WriteLine("1. Opret ny konto");
                Console.WriteLine("2. Hæv/sæt ind");
                Console.WriteLine("3. Se en oversigt");
                Console.WriteLine("0. Afslut");

                Console.Write(">");
                string valg1 = Console.ReadLine();
                int valg = int.Parse(valg1); // Tilføjer 1 til valg før den parser, ender som f.eks. 11 istedet for 1
                switch (valg) {
                    case 1:
                        DosOpretKonto();
                        break;
                    case 2:
                        DosOpretTransaktion(DosFindKonto());
                        break;
                    case 3:
                        DosUdskrivKonto(DosFindKonto());
                        break;
                    case 0:
                        blivVedOgVed = false;
                        break;
                    default:
                        Console.WriteLine("UGYLDIGT VALGT!!");
                        Console.ReadKey();
                        break;

                }
            }
            Console.Clear();
        }
        static Konto DosFindKonto() // Pascal case istedet for en blanding af Camel og Pascal case
        {
            for (var i = 1; i <= konti.Count;i++)
            {
                Console.WriteLine(i+". "+konti[i-1].registreringsnr+" "+konti[i-1].kontonr+" ejes af "+konti[i-1].ejer);
            }
            Console.WriteLine("Vælg et tal fra 1 til "+konti.Count);
            Console.Write(">");
            int tal = int.Parse(Console.ReadLine());
            if (tal < 1 || tal > konti.Count) {
                Console.WriteLine("Ugyldigt valg");
                Console.Clear();
                return null;
            }
            return konti[tal-1];
        }
        static void DosOpretTransaktion(Konto k) 
        {
            Console.Write("Tekst: ");
            string tekst = Console.ReadLine();
            Console.Write("Beløb: ");
            float amount = float.Parse(Console.ReadLine());
            if (GemTrans(k,tekst,amount)) {
                Console.WriteLine("Transkationen blev Gemt. Ny saldo på kontoen: "+FindSaldo(k));
                Gem();
            } else
                Console.WriteLine("Transaktionen kunne ikke Gemmes (Der var sikkert ikke penge nok på kontoen)");
        }
        static Konto DosOpretKonto() 
        {
            Konto k = LavKonto();
            Console.Write("Navn på kontoejer:");
            k.ejer = Console.ReadLine();
            Console.WriteLine("Konto oprettet!");
            konti.Add(k);
            Gem();
            return k;
        }
        public static Konto LavKonto() {
            return new Konto();
        }


        static void DosUdskrivKonti() {
            Console.WriteLine("================");
            foreach (Konto k in konti) {
                Console.WriteLine(k.registreringsnr+" "+k.kontonr+" ejes af "+k.ejer);
            }
        }
        static void DosUdskrivKonto(Konto k) {
            Console.WriteLine("Konto for "+k.ejer+": "+k.registreringsnr+" "+k.kontonr);
            Console.WriteLine("================");
            Console.WriteLine("Tekst\t\t\t\tBeløb\t\tSaldo");
            foreach (Transaktion t in k.transaktioner) {
                Console.Write(t.tekst+"\t\t\t\t");
                Console.Write(t.mængde+"\t\t");
                Console.WriteLine(t.saldo);
            }
            Console.WriteLine("================\n");

        }
        
        public static bool GemTrans(Konto konto, string tekst, float beløb) {
            var saldo = FindSaldo(konto);
            if (saldo + beløb < 0) return false;
            var t = new Transaktion();
            t.tekst = tekst;
            t.mængde = beløb; // belob ændret til beløb, belob fik aldrig en value to t.mængde ville altid blive 0
            t.saldo = t.mængde + saldo;
            t.dato = DateTime.Now;
            
            konto.transaktioner.Add(t);
            return true;
        }
        public static float FindSaldo(Konto k) {
            Transaktion seneste = new Transaktion();
            DateTime senesteDato = DateTime.MinValue;
            foreach(var t in k.transaktioner) {
                if (t.dato > senesteDato) {
                    senesteDato = t.dato;
                    seneste = t;
                }
            }
            return seneste.saldo;
        }
        public static void Gem() 
        {
            File.WriteAllText(datafil,JsonConvert.SerializeObject(konti));
            //File.Delete(datafil); //Fjern debug fil
        }
        public static void Hent()
        {
            datafil = "bank.json"; //Debug - brug en anden datafil til debug ~Konrad
            if (File.Exists(datafil)) {
                string json = File.ReadAllText(datafil);
                konti = JsonConvert.DeserializeObject<List<Konto>>(json);
            } else {
                konti = new List<Konto>();
            }
        }
    }
}
/** 
Koden er lavet til undervisningbrug på TECHCOLLEGE
Voldum Bank og nævnte personer er fiktive.
~Simon Hoxer Bønding
**/
