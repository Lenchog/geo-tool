# asks for the shape, then calls other functions to figure out area and prints it
def area():
    command = ''
    while command != 'q':
        # TODO reduce repeated code
        command = input("Which shape would you like to calculate the area of?\n")
        if 'circle' in command: 
            print(f"It's {areaCircle()} squared units!")
        elif 'square' in command or 'rectangle' in command:
            print(f"It's {areaRectangle()} squared units!")
        elif 'triangle' in command:
            # we can imagine the triangle as simply half a rectangle
            print(f"It's {1/2 * areaRectangle()} squared units!")
        # if the user wants to quit, it's not invalid. however, we don't need to handle the q case
        elif command != 'q':
            print("Invalid command, try again")
        
# takes the width and height to simply calculate the area of a theoretical rectangle
# also useful with triangle calculations
def areaRectangle():
    width = int(input("How wide is your shape?"))
    length = int(input("How tall is your shape?"))
    return width * length

# use πr^2 to calculate the area of the circle
def areaCircle():
    radius = int(input("What is the radius?\n"))
    return math.pi * radius * radius

