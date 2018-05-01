import unittest
import sol_a0944


class TestCountOddDigits(unittest.TestCase):
    def test_count_oddDigits(self):
        self.assertEqual(sol_a0944.count_odd_digits(12345), 3)
        self.assertEqual(sol_a0944.count_odd_digits(13579), 5)
        self.assertEqual(sol_a0944.count_odd_digits(24680), 0)


if __name__ == '__main__':
    unittest.main()

