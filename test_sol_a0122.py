import unittest
import sol_a0122


class TestProfit(unittest.TestCase):
    def test_is_profit(self):
        self.assertEqual(sol_a0122.is_profit(200, 100), 1)
        self.assertEqual(sol_a0122.is_profit(1500, 1000), 0.5)


if __name__ == '__main__':
    unittest.main()
