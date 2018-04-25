import unittest
import sol_a0040


class TestAverage(unittest.TestCase):
    def test_avg_of_5_digits(self):
        self.assertEqual(sol_a0040.avg_of_5_digits(53161), 3.2)


if __name__ == '__main__':
    unittest.main()