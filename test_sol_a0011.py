
import unittest
import sol_a0011


class Test_sol_a0011(unittest.TestCase):

    def test_sum_of_digits(self):
        result = sol_a0011.sum_of_digits(12345)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
