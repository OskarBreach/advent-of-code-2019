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

class TestConditionalJumps(unittest.TestCase):

    def test_first_case(self):
        program = [3,9,8,9,10,9,4,9,99,-1,8]

        computer_a = Computer(program.copy(), [0])
        computer_a.run()
        self.assertEqual(computer_a.get_output(), [0])

        computer_b = Computer(program.copy(), [8])
        computer_b.run()
        self.assertEqual(computer_b.get_output(), [1])

    def test_second_case(self):
        program = [3,9,7,9,10,9,4,9,99,-1,8]

        computer_a = Computer(program.copy(), [7])
        computer_a.run()
        self.assertEqual(computer_a.get_output(), [1])

        computer_b = Computer(program.copy(), [8])
        computer_b.run()
        self.assertEqual(computer_b.get_output(), [0])

    def test_third_case(self):
        program = [3,3,1108,-1,8,3,4,3,99]

        computer_a = Computer(program.copy(), [7])
        computer_a.run()
        self.assertEqual(computer_a.get_output(), [0])

        computer_b = Computer(program.copy(), [8])
        computer_b.run()
        self.assertEqual(computer_b.get_output(), [1])

    def test_forth_case(self):
        program = [3,3,1107,-1,8,3,4,3,99]

        computer_a = Computer(program.copy(), [7])
        computer_a.run()
        self.assertEqual(computer_a.get_output(), [1])

        computer_b = Computer(program.copy(), [8])
        computer_b.run()
        self.assertEqual(computer_b.get_output(), [0])

    def test_fifth_case(self):
        program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]

        computer_a = Computer(program.copy(), [0])
        computer_a.run()
        self.assertEqual(computer_a.get_output(), [0])

        computer_b = Computer(program.copy(), [8])
        computer_b.run()
        self.assertEqual(computer_b.get_output(), [1])

    def test_sixth_case(self):
        program = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]

        computer_a = Computer(program.copy(), [0])
        computer_a.run()
        self.assertEqual(computer_a.get_output(), [0])

        computer_b = Computer(program.copy(), [8])
        computer_b.run()
        self.assertEqual(computer_b.get_output(), [1])

    def test_seventh_case(self):
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, \
            1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105, \
            1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

        computer_a = Computer(program.copy(), [7])
        computer_a.run()
        self.assertEqual(computer_a.get_output(), [999])

        computer_b = Computer(program.copy(), [8])
        computer_b.run()
        self.assertEqual(computer_b.get_output(), [1000])

        computer_c = Computer(program.copy(), [9])
        computer_c.run()
        self.assertEqual(computer_c.get_output(), [1001])

if __name__ == "__main__":
    unittest.main()
