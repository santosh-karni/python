import unittest
import sol_a0124


class TestMinimum(unittest.TestCase):
    def test_my_minimum(self):
        self.assertEqual(sol_a0124.my_minimum(10, 5, 20), 5)
        self.assertEqual(sol_a0124.my_minimum(10, -5, 20), -5)
        self.assertEqual(sol_a0124.my_minimum(0, 0, 0), 0)


if __name__ == '__main__':
    unittest.main()
