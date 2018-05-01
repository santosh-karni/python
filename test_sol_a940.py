import unittest
import sol_a0940


class TestOdd(unittest.TestCase):
    def test_check_if_odd(self):
        self.assertTrue(sol_a0940.check_if_odd(6))
        self.assertFalse(sol_a0940.check_if_odd(5))


if __name__ == '__main__':
    unittest.main()