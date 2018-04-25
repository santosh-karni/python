import unittest
import sol_a0033


class TestConverter(unittest.TestCase):
    def test_convert_kms_to_feet(self):
        self.assertEqual(sol_a0033.convert_kms_to_feet(1), 3280.84)
        self.assertEqual(sol_a0033.convert_kms_to_feet(100), 328084)
        self.assertEqual(sol_a0033.convert_kms_to_feet(0), 0)
        self.assertEqual(sol_a0033.convert_kms_to_feet(-1), -3280.84)


if __name__ == '__main__':
    unittest.main()
