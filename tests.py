import unittest
import math
from area import areaCircle, areaTriangle, areaRectangle
from pythagoras import pythag_maths
from classifyTriangle import classifyTriangle
from lib import validateInt

class TestStringMethods(unittest.TestCase):
    def test_pythag(self):
        self.assertEqual(pythag_maths(3, 4, 'y'), 5)
        self.assertEqual(pythag_maths(5, 4, 'n'), 3)

    def test_circle_area(self):
        self.assertEqual(areaCircle(5), 78.54)
        self.assertEqual(areaCircle(1), 3.14)
        
    def test_triangle_area(self):
        self.assertEqual(areaTriangle(5, 4), 10)
        self.assertEqual(areaTriangle(1, 1), 1/2)
        
    def test_rectangle_area(self):
        self.assertEqual(areaRectangle(5, 4), 20)
        self.assertEqual(areaRectangle(1, 1), 1)

    def test_classify_triangles(self):
        self.assertEqual(classifyTriangle([3, 4, 5]), "Right Angled")
        self.assertEqual(classifyTriangle([3, 3, 3]), "Equilateral")
        self.assertEqual(classifyTriangle([2, 3, 4]), "Scalene")
        self.assertEqual(classifyTriangle([3, 3, 4]), "Isosceles")
        self.assertEqual(classifyTriangle([1, 1, 2]), "Impossible")
        
    # every time an integer is inputted it runs through this.
    # therefore we don't need to test these cases for everything else
    def test_validate_int(self):
        with self.assertRaises(ValueError):
            validateInt("Hello World!")
        with self.assertRaises(Exception):
            validateInt(0)
            # gets converted to 0
            validateInt(0.9)
            validateInt(-1)

if __name__ == '__main__':
    unittest.main()
