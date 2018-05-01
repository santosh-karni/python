import unittest
import sol_a0128


class TestZero(unittest.TestCase):
    def test_is_zero(self):
        self.assertTrue(sol_a0128.is_zero(0))
        self.assertFalse(sol_a0128.is_zero(1))


if __name__ == '__main__':
    unittest.main()
