import unittest
import sol_a0941


class TestEven(unittest.TestCase):
    def test_is_even(self):
        self.assertFalse(sol_a0941.is_even(4))
        self.assertTrue(sol_a0941.is_even(5))


if __name__ == '__main__':
    unittest.main()
