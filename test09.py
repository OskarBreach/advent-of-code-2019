import unittest
from day02 import Computer


class TestNewFeatures(unittest.TestCase):

    def test_firstTestCase(self):
        computer = Computer([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
        computer.run()

        self.assertEqual(computer.get_output(), [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])

    def test_secondTestCase(self):
        computer = Computer([1102,34915192,34915192,7,4,7,99,0])
        computer.run()

        self.assertEqual(computer.get_output(), [1219070632396864])

    def test_thirdTestCase(self):
        computer = Computer([104,1125899906842624,99])
        computer.run()

        self.assertEqual(computer.get_output(), [1125899906842624])


if __name__ == "__main__":
    unittest.main()
