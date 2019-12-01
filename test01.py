import unittest
from day01 import fuel_required, total_fuel_required


class FuelRequiredTests(unittest.TestCase):

    def test_firstTestCase(self):
        self.assertEqual(fuel_required(12), 2)

    def test_secondTestCase(self):
        self.assertEqual(fuel_required(14), 2)

    def test_thirdTestCase(self):
        self.assertEqual(fuel_required(1969), 654)

    def test_forthTestCase(self):
        self.assertEqual(fuel_required(100756), 33583)


class TotalFuelRequiredTests(unittest.TestCase):

    def test_firstTestCase(self):
        self.assertEqual(total_fuel_required(12), 2)

    def test_secondTestCase(self):
        self.assertEqual(total_fuel_required(1969), 966)

    def test_thirdTestCase(self):
        self.assertEqual(total_fuel_required(100756), 50346)


if __name__ == "__main__":
    unittest.main()