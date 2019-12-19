import unittest
from day13 import draw_screen, count_blocks, get_ball, get_paddle
from collections import defaultdict

class MockComputer:
    def __init__(self):
        self.halted = False
        self.expected_outputs = []
        self.outputs = []

    def get_output(self):
        return self.outputs

    def run(self):
        self.outputs = self.expected_outputs
        self.expected_outputs = []
        self.halted = True            

class TestScreenDrawing(unittest.TestCase):

    def test_no_output(self):
        computer = MockComputer()
        computer.expected_outputs = []
        screen = defaultdict(lambda: defaultdict(int))
        draw_screen(computer, screen)

        self.assertEqual(count_blocks(screen), 0)

    def test_given_example(self):
        computer = MockComputer()
        computer.expected_outputs = [1, 2, 3, 6, 5, 4]
        screen = defaultdict(lambda: defaultdict(int))
        draw_screen(computer, screen)

        self.assertEqual(count_blocks(screen), 0)

    def test_overwritten(self):
        computer = MockComputer()
        computer.expected_outputs = [1, 2, 2, 1, 2, 2]
        screen = defaultdict(lambda: defaultdict(int))
        draw_screen(computer, screen)

        self.assertEqual(count_blocks(screen), 1)

    def test_multiple_blocks(self):
        computer = MockComputer()
        computer.expected_outputs = [1, 2, 2, 7, 8, 2]
        screen = defaultdict(lambda: defaultdict(int))
        draw_screen(computer, screen)

        self.assertEqual(count_blocks(screen), 2)


class TestGetBallPaddle(unittest.TestCase):

    def test_no_output(self):
        computer = MockComputer()
        computer.expected_outputs = [1, 2, 2, 7, 8, 2]
        screen = defaultdict(lambda: defaultdict(int))
        draw_screen(computer, screen)

        self.assertEqual(get_ball(screen), None)
        self.assertEqual(get_paddle(screen), None)

    def test_given_example(self):
        computer = MockComputer()
        computer.expected_outputs = [1, 2, 3, 6, 5, 4]
        screen = defaultdict(lambda: defaultdict(int))
        draw_screen(computer, screen)

        self.assertEqual(get_ball(screen), 6)
        self.assertEqual(get_paddle(screen), 1)

if __name__ == "__main__":
    unittest.main()
