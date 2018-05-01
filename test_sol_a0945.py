import unittest
import sol_a0945


class TestCountEvenDigits(unittest.TestCase):
    def test_count_evenDigits(self):
        self.assertEqual(sol_a0945.count_even_digits(12345), 2)
        self.assertEqual(sol_a0945.count_even_digits(17395), 0)


if __name__ == '__main__':
    unittest.main()
