"""Test case to get Circumference of a Circle  """
import unittest
import sol_a0019


class TestSol(unittest.TestCase):
    """ simple class for circumference"""
    def test_get_circumference(self):
        """ Function to write a test case """
        result = sol_a0019.get_circumference(20)
        self.assertEqual(result, 125.67999999999999)


if __name__ == '__main__':
    unittest.main()
