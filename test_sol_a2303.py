import unittest
import sol_a2303


class TestProduct(unittest.TestCase):
    def test_product(self):
        self.assertEqual(sol_a2303.product(200,3), 600)


if __name__ == '__main__':
    unittest.main()
