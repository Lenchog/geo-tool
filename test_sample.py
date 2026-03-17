import unittest
from geoTool.lib import validateInt
from geoTool.area import areaCircle, areaTriangle, areaRectangle
from geoTool.pythagoras import pythag_maths
from geoTool.classifyTriangle import classifyTriangle


class TestStringMethods(unittest.TestCase):
    def test_pythag(self):
        # test finding the hypotenuse
        self.assertEqual(pythag_maths(3, 4, "y"), 5)
        # test finding a different side
        self.assertEqual(pythag_maths(5, 4, "n"), 3)

    def test_circle_area(self):
        # area of large circle
        self.assertEqual(areaCircle(5), 78.54)
        # area of small circle
        self.assertEqual(areaCircle(1), 3.14)

    def test_triangle_area(self):
        # area of large triangle
        self.assertEqual(areaTriangle(5, 4), 10)
        # area of small triangle
        self.assertEqual(areaTriangle(1, 1), 1 / 2)

    def test_rectangle_area(self):
        # area of large rectangle
        self.assertEqual(areaRectangle(5, 4), 20)
        # area of small square
        self.assertEqual(areaRectangle(1, 1), 1)

    # every time an integer is inputted it runs through this.
    # therefore we don't need to test these cases for everything else
    def test_validate_int(self):
        with self.assertRaises(ValueError):
            # test string
            validateInt("Hello World!")
        with self.assertRaises(Exception):
            # test numbers smaller than or equal to 0
            validateInt(0)
            # gets converted to 0
            validateInt(0.9)
            validateInt(-1)


if __name__ == "__main__":
    unittest.main()
