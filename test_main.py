import unittest
from unittest import TestCase
import main
import csv


class Test(TestCase):

    def odczyt(nrKolumnyDoTestu):
        kolumnaDoTestu = []

        with open("details.csv", "r", encoding="utf-8") as readCSV:
            read = csv.reader(readCSV)
            for line in read:
                kolumnaDoTestu.append(line[nrKolumnyDoTestu])

        return kolumnaDoTestu

    def test_read_csvfile(self):
        read_csv_file = main.odczyt(0)
        kolumnaDoTestu = Test.odczyt(0)

        self.assertEqual(read_csv_file, kolumnaDoTestu)

    def test_kolumna1(self):
        self.assertEqual(main.kolumna1(), Test.odczyt(0))

    def test_kolumna2(self):
        self.assertEqual(main.kolumna2(), Test.odczyt(1))

    def test_kolumna3(self):
        self.assertEqual(main.kolumna3(), Test.odczyt(2))

    def test_kolumna4(self):
        self.assertEqual(main.kolumna4(), Test.odczyt(3))

    def test_kolumna5(self):
        self.assertEqual(main.kolumna5(), Test.odczyt(4))

    def test_kolumna6(self):
        self.assertEqual(main.kolumna6(), Test.odczyt(5))

    def test_kolumna7(self):
        self.assertEqual(main.kolumna7(), Test.odczyt(7))   #iteracja zmienila sie o 2 poniewaz 7 kolumny mielismy nie robic

    def test_kolumna8(self):
        self.assertEqual(main.kolumna8(), Test.odczyt(8))

    def test_kolumna9(self):
        self.assertEqual(main.kolumna9(), Test.odczyt(9))

if __name__ == '__main__':
    unittest.main()




