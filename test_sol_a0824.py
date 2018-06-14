import unittest
import sol_a0824


class findPow(unittest.TestCase):
    def test_find_pow(self):
        self.assertEqual(sol_a0824.find_pow(2, 2), 4)
        self.assertEqual(sol_a0824.find_pow(5, 3), 125)
        self.assertEqual(sol_a0824.find_pow(8, -1), 0.125)


if __name__ == '__main__':
    unittest.main()
