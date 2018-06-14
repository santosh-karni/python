import unittest
import sol_a0666


class Sum_of_N(unittest.TestCase):
    def test_find_sum_till_n(self):
        self.assertEqual(sol_a0666.find_sum_till_n(4), 10)


if __name__ == '__main__':
    unittest.main()
