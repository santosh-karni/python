import unittest
import sol_a2246


class sumEvenFibonacci(unittest.TestCase):
    def test_sum_of_even_fibonacci(self):
        self.assertEqual(sol_a2246.find_sum_of_even_numbers_fibonacci(5), 10)


if __name__ == '__main__':
    unittest.main()
