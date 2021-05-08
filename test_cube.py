import unittest
import cube

class testCube(unittest.TestCase):
    def test_cube_1(self):
        self.assertEqual(cube.volume(3),27)

    def test_cube_2(self):
        self.assertEqual(cube.volume(-2),-8)

    def test_cube_3(self):
        self.assertIsInstance(cube.volume('asdf'),str)

if __name__ == "__main__":
    unittest.main()                                                                                                                                                             

