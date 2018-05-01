import unittest
import sol_a2202


class TestMax(unittest.TestCase):
    def test_mymax(self):
        self.assertEqual(sol_a2202.mymax(5, 6), 6)
        self.assertFalse(sol_a2202.mymax(5, 5))


if __name__ == '__main__':
    unittest.main()
