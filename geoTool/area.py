from geoTool.lib import getInt
import math

# asks for the shape, then calls other functions to figure out area and prints it
def area():
    while True:
        # for each we ask for the variables we need, and print the result
        command = input("Which shape would you like to calculate the area of?\n")
        if 'circle' in command: 
            radius = getInt("What is the radius?")
            area = areaCircle(radius)
        elif 'square' in command :
            width = getInt("Give a side length of the square")
            area = areaRectangle(width, width)
        elif 'triangle' in command:
            height = getInt("How tall is the triangle?")
            base = getInt("How wide is the base of the triangle?")
            area = areaTriangle(height, base)
        elif 'rectangle' in command:
            width = getInt("How wide is your rectangle?")
            length = getInt("How tall is your rectangle?")
            area = areaRectangle(width, length)
        # if the user wants to quit, it's not invalid. however, we don't need to handle the q case
        else:
            break;
        print(f"It's {area} squared units!")
        
# 1/2 * base * height
def areaTriangle(base, height):
    return 1/2 * base * height

# takes the width and height to simply calculate the area of a theoretical rectangle
# also useful with triangle calculations
def areaRectangle(width: int, length: int):
    return width * length

# use πr^2 to calculate the area of the circle
def areaCircle(radius: int):
    return round(math.pi * radius**2, 2)

