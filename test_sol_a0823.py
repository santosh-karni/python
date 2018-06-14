import unittest
import sol_a0823


class CalculateFactorial(unittest.TestCase):
    def test_calculate_factorial(self):
        self.assertEqual(sol_a0823.calculate_factorial(3), 6)
        self.assertEqual(sol_a0823.calculate_factorial(1), 1)
        self.assertEqual(sol_a0823.calculate_factorial(0), 1)


if __name__ == '__main__':
    unittest.main()
