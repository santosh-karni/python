""" simple class to reverse a number"""
from sol_a0010 import reverse_5_digit_int
import unittest


class TestRev(unittest.TestCase):
    """ Reversing a number """
    def test_reverse_5_digit_int(self):
        """Function to write test case """
        result = reverse_5_digit_int(12345)
        self.assertEqual(result, 54321)


if __name__ == '__main__':
    unittest.main()