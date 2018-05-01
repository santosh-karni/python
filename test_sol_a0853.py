import unittest
import sol_a0853


class TestLeapYear(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(sol_a0853.is_leap_year(2016))
        self.assertFalse(sol_a0853.is_leap_year(-2016))
        self.assertFalse(sol_a0853.is_leap_year(2017))


if __name__ == '__main__':
    unittest.main()

