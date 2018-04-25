import unittest
import sol_a2300


class Add2Numbers(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(sol_a2300.add_two_numbers(5,6), 11)


if __name__ == '__main__':
    unittest.main()
