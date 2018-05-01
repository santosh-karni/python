import unittest
import sol_a2203


class TestMax3(unittest.TestCase):
    def test_max_of_three(self):
        self.assertEqual(sol_a2203.max_of_three(7, 6, 5), 7)
        self.assertEqual(sol_a2203.max_of_three(5, 7, 6), 7)
        self.assertEqual(sol_a2203.max_of_three(5, 6, 7), 7)
        self.assertEqual(sol_a2203.max_of_three(-5, -6, -7), -5)
        self.assertFalse(sol_a2203.max_of_three(5, 5, 5))


if __name__ == '__main__':
    unittest.main()
