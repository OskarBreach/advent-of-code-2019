import unittest
from day10 import best_location, get_asteroids, get_visible, vaporize_order


class TestAsteroidDetect(unittest.TestCase):

    def test_firstTestCase(self):
        asteroids = [".#..#",
            ".....",
            "#####",
            "....#",
            "...##"]

        self.assertEqual(best_location(asteroids), (3, 4, 8))


    def test_secondTestCase(self):
        asteroids = ["......#.#.",
            "#..#.#....",
            "..#######.",
            ".#.#.###..",
            ".#..#.....",
            "..#....#.#",
            "#..#....#.",
            ".##.#..###",
            "##...#..#.",
            ".#....####"]

        self.assertEqual(best_location(asteroids), (5, 8, 33))

    def test_thirdTestCase(self):
        asteroids = ["#.#...#.#.",
            ".###....#.",
            ".#....#...",
            "##.#.#.#.#",
            "....#.#.#.",
            ".##..###.#",
            "..#...##..",
            "..##....##",
            "......#...",
            ".####.###."]

        self.assertEqual(best_location(asteroids), (1, 2, 35))

    def test_forthTestCase(self):
        asteroids = [".#..#..###",
            "####.###.#",
            "....###.#.",
            "..###.##.#",
            "##.##.#.#.",
            "....###..#",
            "..#.#..#.#",
            "#..#.#.###",
            ".##...##.#",
            ".....#.#.."]

        self.assertEqual(best_location(asteroids), (6, 3, 41))

    def test_fifthTestCase(self):
        asteroids = [".#..##.###...#######",
            "##.############..##.",
            ".#.######.########.#",
            ".###.#######.####.#.",
            "#####.##.#.##.###.##",
            "..#####..#.#########",
            "####################",
            "#.####....###.#.#.##",
            "##.#################",
            "#####.##.###..####..",
            "..######..##.#######",
            "####.##.####...##..#",
            ".#####..#.######.###",
            "##...#.##########...",
            "#.##########.#######",
            ".####.#.###.###.#.##",
            "....##.##.###..#####",
            ".#.#.###########.###",
            "#.#.#.#####.####.###",
            "###.##.####.##.#..##"]

        self.assertEqual(best_location(asteroids), (11, 13, 210))

class TestVaporizeOrder(unittest.TestCase):

    def test_case(self):
        asteroids = [".#..##.###...#######",
            "##.############..##.",
            ".#.######.########.#",
            ".###.#######.####.#.",
            "#####.##.#.##.###.##",
            "..#####..#.#########",
            "####################",
            "#.####....###.#.#.##",
            "##.#################",
            "#####.##.###..####..",
            "..######..##.#######",
            "####.##.####...##..#",
            ".#####..#.######.###",
            "##...#.##########...",
            "#.##########.#######",
            ".####.#.###.###.#.##",
            "....##.##.###..#####",
            ".#.#.###########.###",
            "#.#.#.#####.####.###",
            "###.##.####.##.#..##"]

        order = vaporize_order(asteroids)

        self.assertEqual(order[0], (11, 12))
        self.assertEqual(order[1], (12, 1))
        self.assertEqual(order[2], (12, 2))
        self.assertEqual(order[9], (12, 8))
        self.assertEqual(order[19], (16, 0))
        self.assertEqual(order[49], (16, 9))
        self.assertEqual(order[99], (10, 16))
        self.assertEqual(order[198], (9, 6))
        self.assertEqual(order[199], (8, 2))
        self.assertEqual(order[200], (10, 9))
        self.assertEqual(order[298], (11, 1))


if __name__ == "__main__":
    unittest.main()
