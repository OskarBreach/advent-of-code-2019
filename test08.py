import unittest
from day08 import signal_checksum, translate_signal


class TestSignalChecksum(unittest.TestCase):

    def test_first_case(self):
        self.assertEqual(signal_checksum('123456789012', 3, 2), 1)

    def test_second_case(self):
        self.assertEqual(signal_checksum('01234567012345671111222222223333', 4, 4), 32)


class TranslateSignal(unittest.TestCase):

    def test_first_case(self):
        self.assertEqual(translate_signal('0222112222120000', 2, 2), '01\n10')

    def test_second_case(self):
        self.assertEqual(translate_signal('222222222101010101', 3, 3), '101\n010\n101')

if __name__ == "__main__":
    unittest.main()