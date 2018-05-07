import unittest
import sol_a0940


class TestOdd(unittest.TestCase):
    def test_check_if_odd(self):
        self.assertEqual(sol_a0940.check_if_odd(3), 0)


if __name__ == '__main__':
    unittest.main()
