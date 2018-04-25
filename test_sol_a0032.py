import unittest
import sol_a0032


class TestConverter(unittest.TestCase):
    def test_convert_kms_to_mms(self):
        self.assertEqual(sol_a0032.convert_kms_to_mms(1), 1000000)
        self.assertEqual(sol_a0032.convert_kms_to_mms(-1), -1000000)
        self.assertEqual(sol_a0032.convert_kms_to_mms(0), 0)


if __name__ == '__main__':
    unittest.main()