import unittest
import sol_a0129


class TestMax4(unittest.TestCase):
    def test_find_maximum_in_4(self):
        self.assertEqual((sol_a0129.find_maximum_in_4(1, 2, 3, 4)), 4.0)


if __name__ == '__main__':
    unittest.main()
