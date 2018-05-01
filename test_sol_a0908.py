import unittest
import sol_a0908


class TestMultiple3(unittest.TestCase):
    def test_is_multiple_of_3(self):
        self.assertEqual(sol_a0908.is_multiple_of_3(21), 0)
        self.assertEqual(sol_a0908.is_multiple_of_3(13), -1)


if __name__ == '__main__':
    unittest.main()
