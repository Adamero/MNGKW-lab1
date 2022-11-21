import csv
import unittest

from main import Excel


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.csvreader = csv.reader(open("details.csv", 'r', encoding="utf-8"))

    def test_publisher(self):
        for row in self.csvreader:
            with self.subTest():
                # given
                publisher_value = row[0]
                details_value = row[1]
                no = row[2]
                # then
                extractor = Excel(publisher_value, details_value)
                # expect
                self.assertEqual(extractor.publisher(), publisher_value)

    def test_details(self):
        for row in self.csvreader:
            with self.subTest():
                # given
                publisher_value = row[0]
                details_value = row[1]
                no = row[2]
                # then
                extractor = Excel(publisher_value, details_value)
                # expect
                self.assertEqual(extractor.details(), details_value)

    def test_no(self):
        for row in self.csvreader:
            with self.subTest():
                # given
                publisher_value = row[0]
                details_value = row[1]
                no = row[2]
                # then
                extractor = Excel(publisher_value, details_value)
                # expect
                self.assertEqual(extractor.no(), no)

    def test_vol(self):
        for row in self.csvreader:
            with self.subTest():
                # given
                publisher_value = row[0]
                details_value = row[1]
                vol = row[3]
                # then
                extractor = Excel(publisher_value, details_value)
                # expect
                self.assertEqual(extractor.vol(),vol)

    def test_articleNo(self):
        for row in self.csvreader:
            with self.subTest():
                # given
                publisher_value = row[0]
                details_value = row[1]
                articleNo = row[4]
                # then
                extractor = Excel(publisher_value, details_value)
                # expect
                self.assertEqual(extractor.vol(), articleNo)

    def test_pagesInRange(self):
        for row in self.csvreader:
            with self.subTest():
                # given
                publisher_value = row[0]
                details_value = row[1]
                pagesInRange = row[5]
                # then
                extractor = Excel(publisher_value, details_value)
                # expect
                self.assertEqual(extractor.pagesInRange(), pagesInRange)

    def test_publisherName(self):
        for row in self.csvreader:
            with self.subTest():
                # given
                publisher_value = row[0]
                details_value = row[1]
                publisherName = row[7]
                # then
                extractor = Excel(publisher_value, details_value)
                # expect
                self.assertEqual(extractor.publisherName(), publisherName)

    def test_publisherLocation(self):
        for row in self.csvreader:
            with self.subTest():
                # given
                publisher_value = row[0]
                details_value = row[1]
                publisherLocation = row[8]
                # then
                extractor = Excel(publisher_value, details_value)
                # expect
                self.assertEqual(extractor.publisherLocation(), publisherLocation)

    def publisherYear(self):
        for row in self.csvreader:
            with self.subTest():
                # given
                publisher_value = row[0]
                details_value = row[1]
                publisherYear = row[9]
                # then
                extractor = Excel(publisher_value, details_value)
                # expect
                self.assertEqual(extractor.publisherYear(), publisherYear)

if __name__ == '__main__':
    unittest.main()