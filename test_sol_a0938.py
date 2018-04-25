import unittest
import sol_a0938


class TestNumber(unittest.TestCase):
    def test_make_number_from_5_digits(self):
        self.assertEqual(sol_a0938.make_number_from_5_digits(1,2,3,4,5), 12345)


if __name__ == '__main__':
    unittest.main()
