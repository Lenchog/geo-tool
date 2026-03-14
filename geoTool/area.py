from geoTool.lib import getInt
import math


# asks for the shape, then calls other functions to figure out area and prints it
def area():
    while True:
        # for each we ask for the variables we need, and print the result
        print("Which shape would you like to calculate the area of?")
        shape = input("Circle, square, rectangle or triangle\n")
        # look at the first letter of the input to catch a wide variety of cases
        match shape[0].lower():
            case "c":  # circle
                radius = getInt("What is the radius?")
                area = areaCircle(radius)
            case "s":  # square
                width = getInt("Give a side length of the square")
                area = areaRectangle(width, width)
            case "t":  # triangle
                height = getInt("How tall is the triangle?")
                base = getInt("How wide is the base of the triangle?")
                area = areaTriangle(height, base)
            case "r":  # rectangle
                width = getInt("How wide is your rectangle?")
                height = getInt("How tall is your rectangle?")
                area = areaRectangle(width, height)
            # otherwise quit, it's not invalid. however, we don't need to handle the q case
            case _:
                break
        print(f"It's {area} squared units!")


# 1/2 * base * height
def areaTriangle(base, height):
    return 1 / 2 * base * height


# takes the width and height to simply calculate the area of a theoretical rectangle
# also useful with triangle calculations
def areaRectangle(width: int, length: int):
    return width * length


# use πr^2 to calculate the area of the circle
def areaCircle(radius: int):
    return round(math.pi * radius**2, 2)
