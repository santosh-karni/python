""" simple class to reverse a number"""
import unittest
import sol_a0010


class TestRev(unittest.TestCase):
    """ Reversing a number """
    def test_reverse_5_digit_int(self):
        """Function to write testcase """
        result = sol_a0010.reverse_5_digit_int(12345)
        self.assertEqual(result, 54321)


if __name__ == '__main__':
    unittest.main()