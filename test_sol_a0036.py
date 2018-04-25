import unittest
import sol_a0036


class TestFC(unittest.TestCase):
    def test_convert_fahrenheit_to_celsius(self):
        self.assertEqual(sol_a0036.convert_fahrenheit_to_celsius(68), 20)
        self.assertEqual(sol_a0036.convert_fahrenheit_to_celsius(-68), -55.55555555555556)
        self.assertEqual(sol_a0036.convert_fahrenheit_to_celsius(0), -17.77777777777778)
        self.assertEqual(sol_a0036.convert_fahrenheit_to_celsius(32), 0)


if __name__ == '__main__':
    unittest.main()
