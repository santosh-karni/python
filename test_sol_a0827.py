import unittest
import sol_a0827


class genFibonacci(unittest.TestCase):
    def test_gen_fibonacci(self):
        self.assertEqual(sol_a0827.gen_fibonacci(5),3)


if __name__ == '__main__':
    unittest.main()
