import unittest
import sol_a0130


class TestFindGrade(unittest.TestCase):
    def test_find_grade(self):
        self.assertEqual(sol_a0130.find_grade(60), "Grade 3")


if __name__ == '__main__':
    unittest.main()
