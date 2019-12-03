import unittest
from day03 import closest_intersection, fewest_steps


class ClosestIntersectionTests(unittest.TestCase):

    def test_firstTestCase(self):
        self.assertEqual(closest_intersection(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']), 6)

    def test_secondTestCase(self):
        self.assertEqual(closest_intersection(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'], 
        ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']), 159)
        
    def test_thirdTestCase(self):
        self.assertEqual(closest_intersection(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'], 
        ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']), 135)        


class FewestStepsTests(unittest.TestCase):

    def test_firstTestCase(self):
        self.assertEqual(fewest_steps(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']), 30)

    def test_secondTestCase(self):
        self.assertEqual(fewest_steps(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'], 
        ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']), 610)
        
    def test_thirdTestCase(self):
        self.assertEqual(fewest_steps(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'], 
        ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']), 410)       


if __name__ == "__main__":
    unittest.main()