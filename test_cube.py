import unittest
import cube

class testCube(unittest.TestCase):
    def test_cube_1(self):
        self.assertEqual(cube.cube(3),27)

    def test_cube_2(self):
        self.assertEqual(cube.cube(-2),-8)

    # def test_cube_3(self):
    #     self.assertEqual(cube.cube(a),error)

if __name__ == "__main__"
    unittest.main()                                                                                                                                                             

