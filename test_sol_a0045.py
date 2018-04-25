import unittest
import sol_a0045


class TestCubeVolume(unittest.TestCase):
    def test_cub_volume(self):
        self.assertEqual(sol_a0045.cub_volume(5), 125)


if __name__ == '__main__':
    unittest.main()
