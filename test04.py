import unittest
from day04 import password_candidate, enhanced_password_candidate


class PasswordCandidateTests(unittest.TestCase):

    def test_valid_password(self):
        self.assertEqual(password_candidate(111111), True)

    def test_other_valid_password(self):
       self.assertEqual(password_candidate(122345), True)

    def test_password_short(self):
        self.assertEqual(password_candidate(11111), False)

    def test_password_long(self):
        self.assertEqual(password_candidate(1111111), False)

    def test_decreasing_digit(self):
        self.assertEqual(password_candidate(223450), False)

    def test_other_decreasing_digit(self):
        self.assertEqual(password_candidate(134437), False)

    def test_not_double_digit(self):
        self.assertEqual(password_candidate(123789), False)

    def test_other_not_double_digit(self):
        self.assertEqual(password_candidate(135679), False)


class ContainsAnExactDoubleGroup(unittest.TestCase):

    def test_existing_bad_passwords_are_bad(self):
        self.assertEqual(enhanced_password_candidate(11111), False)
        self.assertEqual(enhanced_password_candidate(1111111), False)
        self.assertEqual(enhanced_password_candidate(223450), False)
        self.assertEqual(enhanced_password_candidate(134437), False)
        self.assertEqual(enhanced_password_candidate(123789), False)
        self.assertEqual(enhanced_password_candidate(135679), False)

    def test_some_existing_good_passwords_are_good(self):
        self.assertEqual(enhanced_password_candidate(122345), True)

    def test_contains_double(self):
        self.assertEqual(enhanced_password_candidate(112233), True)

    def test_other_contains_double(self):
        self.assertEqual(enhanced_password_candidate(111122), True)

    def test_contains_no_double(self):
        self.assertEqual(enhanced_password_candidate(123444), False)

    def test_other_contains_no_double(self):
        self.assertEqual(enhanced_password_candidate(111111), False)


if __name__ == "__main__":
    unittest.main()
