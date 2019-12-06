import unittest
from day06 import count_orbits, count_transfers


class TestOrbitCounting(unittest.TestCase):

    def test_single_orbit(self):
        self.assertEqual(count_orbits(['COM)B']), 1)

    def test_complicated_orbits(self):
        orbit_list = ['COM)B',
            'B)C',
            'C)D',
            'D)E',
            'E)F',
            'B)G',
            'G)H',
            'D)I',
            'E)J',
            'J)K',
            'K)L']

        self.assertEqual(count_orbits(orbit_list), 42)

    def test_complicated_orbits_out_of_order(self):
        orbit_list = ['B)C',
            'D)I',
            'E)J',
            'J)K',
            'COM)B',
            'K)L',
            'C)D',
            'D)E',
            'E)F',
            'B)G',
            'G)H',]

        self.assertEqual(count_orbits(orbit_list), 42)


class TestOrbitTransfers(unittest.TestCase):

    def test_simple_orbit_transfer(self):
        self.assertEqual(count_transfers(['COM)SAN', 'B)YOU', 'COM)B']), 1)

    def test_complicated_orbit_transfer(self):
        orbit_list = ['B)C',
            'D)I',
            'I)SAN',
            'E)J',
            'K)YOU',
            'J)K',
            'COM)B',
            'K)L',
            'C)D',
            'D)E',
            'E)F',
            'B)G',
            'G)H',]

        self.assertEqual(count_transfers(orbit_list), 4)

if __name__ == "__main__":
    unittest.main()
