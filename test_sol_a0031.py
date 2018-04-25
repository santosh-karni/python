import unittest
import sol_a0031


class TestSalary(unittest.TestCase):
    def test_calculate_gross_salary(self):
        self.assertEqual(sol_a0031.calculate_gross_salary(20000, 10, 5000), 27000)
        self.assertEqual(sol_a0031.calculate_gross_salary(40000, 10, 5000), 49000)


if __name__ == '__man__':
    unittest.main()
