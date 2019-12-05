import unittest
from day02 import Computer


class TestImmediateMode(unittest.TestCase):

    def test_immediate_add(self):
        computer = Computer([1001, 2, 1, 0, 99])
        computer.run()

        self.assertEqual(computer.memory, [2, 2, 1, 0, 99])

    def test_other_immediate_add(self):
        computer = Computer([1101, 3, 3, 0, 99])
        computer.run()

        self.assertEqual(computer.memory, [6, 3, 3, 0, 99])

    def test_immediate_multiply(self):
        computer = Computer([1002, 4, 3, 4, 33])
        computer.run()

        self.assertEqual(computer.memory, [1002, 4, 3, 4, 99])

    def test_other_immediate_multiply(self):
        computer = Computer([102, 4, 1, 0, 99])
        computer.run()

        self.assertEqual(computer.memory, [16, 4, 1, 0, 99])

class TestInputAndOutput(unittest.TestCase):

    def test_empty_output(self):
        computer = Computer([1, 0, 0, 0, 99])
        computer.run()

        self.assertEqual(computer.get_output(), [])

    def test_single_output(self):
        computer = Computer([4, 0, 99])
        computer.run()

        self.assertEqual(computer.get_output(), [4])

    def test_double_output(self):
        computer = Computer([4, 2, 104, 2, 99])
        computer.run()

        self.assertEqual(computer.get_output(), [104, 2])

    def test_input(self):
        computer = Computer([3, 0, 99], [1])
        computer.run()

        self.assertEqual(computer.memory, [1, 0, 99])

    def test_double_input(self):
        computer = Computer([3, 1, 3, 3, 99], [2, 4])
        computer.run()

        self.assertEqual(computer.memory, [3, 2, 3, 4, 99])

if __name__ == "__main__":
    unittest.main()
