import unittest
from day11 import paint_grid, squares_painted, grid_drawing
from collections import defaultdict



class MockHaltedComputer:
    def __init__(self):
        self.halted = True

    def add_input(self, input):
        pass

    def get_output(self):
        pass

    def run(self):
        pass

class MockExampleComputer:
    def __init__(self):
        self.halted = False
        self.expected_outputs = [(1, 0), (0, 0), (1, 0), (1, 0), (0, 1), (1, 0), (1, 0)]
        self.expected_inputs = [0, 0, 0, 0, 1, 0, 0]
        self.input = None
        self.outputs = []

    def add_input(self, input):
        self.input = input[0]

    def get_output(self):
        return self.outputs

    def run(self):
        if self.input == self.expected_inputs.pop(0):
            self.input = None
            output = self.expected_outputs.pop(0)
            self.outputs = [output[0], output[1]]

            if len(self.expected_outputs) == 0:
                self.halted = True            
        else:
            raise RuntimeError


class TestPaintingRobots(unittest.TestCase):

    def test_always_halted(self):
        computer = MockHaltedComputer()
        grid = defaultdict(lambda: defaultdict(int))
        paint_grid(computer, grid)

        self.assertEqual(squares_painted(grid), 0)

    def test_example_computer(self):
        computer = MockExampleComputer()
        grid = defaultdict(lambda: defaultdict(int))
        paint_grid(computer, grid)

        self.assertEqual(squares_painted(grid), 6)

class TestDrawings(unittest.TestCase):

    def test_example_computer(self):
        computer = MockExampleComputer()
        grid = defaultdict(lambda: defaultdict(int))
        grid[-1][1] = 1

        paint_grid(computer, grid)

        self.assertEqual(grid_drawing(grid), ['#.#', '..#', '##.'])

if __name__ == "__main__":
    unittest.main()
