from lib import getInt
import math

# asks for the shape, then calls other functions to figure out area and prints it
def area():
    command = ''
    while command != 'q':
        command = input("Which shape would you like to calculate the area of?\n")
        if 'circle' in command: 
            radius = getInt("What is the radius?")
            print(f"It's {areaCircle(radius)} squared units!")
        elif 'square' in command :
            width = getInt("Give a side length of the square")
            print(f"It's {areaRectangle(width, width)} squared units!")
        elif 'triangle' in command:
            height = getInt("How tall is the triangle?")
            base = getInt("How wide is the base of the triangle?")
            print(f"It's {areaTriangle(height, base)} squared units!")
        elif 'rectangle' in command:
            width = getInt("How wide is your rectangle?")
            length = getInt("How tall is your rectangle?")
            print(f"It's {areaRectangle(width, length)} squared units!")
        # if the user wants to quit, it's not invalid. however, we don't need to handle the q case
        elif command != 'q':
            print("Invalid command, try again")
        
# 1/2 * base * height
def areaTriangle(base, height):
    return round(1/2 * base * height, 2)

# takes the width and height to simply calculate the area of a theoretical rectangle
# also useful with triangle calculations
def areaRectangle(width: int, length: int):
    return round(width * length, 2)

# use πr^2 to calculate the area of the circle
def areaCircle(radius: int):
    return round(math.pi * radius * radius, 2)

