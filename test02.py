import unittest
from day02 import run_program


class RunProgramStates(unittest.TestCase):

    def test_add(self):
        memory = [1, 0, 0, 0, 99]
        run_program(memory)

        self.assertEqual(memory, [2, 0, 0, 0, 99])

    def test_multiply(self):
        memory = [2, 3, 0, 3, 99]
        run_program(memory)

        self.assertEqual(memory, [2, 3, 0, 6, 99])

    def test_other_multiply(self):
        memory = [2, 4, 4, 5, 99, 0]
        run_program(memory)

        self.assertEqual(memory, [2, 4, 4, 5, 99, 9801])

    def test_multiple_instructions(self):
        memory = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        run_program(memory)

        self.assertEqual(memory, [30, 1, 1, 4, 2, 5, 6, 0, 99])

    def test_non_instruction_halts(self):
        memory = [98, 0, 0, 0, 99]
        run_program(memory)

        self.assertEqual(memory, [98, 0, 0, 0, 99])

if __name__ == "__main__":
    unittest.main()
