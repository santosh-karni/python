import unittest
import sol_a0044


class TestPalindrome(unittest.TestCase):
    def test_palindrome_number(self):
        self.assertEqual(sol_a0044.is_palindrome_number(12321), 0)
        self.assertEqual(sol_a0044.is_palindrome_number(-12321), -1)
        self.assertEqual(sol_a0044.is_palindrome_number(12345), -1)


if __name__ == '__main__':
    unittest.main()
