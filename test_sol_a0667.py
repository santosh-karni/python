import unittest
import sol_a0667


class nthElementGP(unittest.TestCase):
    def test_find_nth_element_in_gp(self):
        self.assertEqual(sol_a0667.find_nth_element_in_gp(2, 2, 3), 16)


if __name__ == '__main__':
    unittest.main()
