import math

# TODO figure out how to use multiple files. way too cluttered

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

# we take two sides and whether either is a hypotenuse,
# then use pythagoras' theorem to calculate what's missing
def pythogoras():
    side1 = int(input("Give me one side of the triangle\n"))
    side2 = int(input("Alright, how long is it?\n"))
    # are we trying to find the hypotenuse, or another side? if so, different formula
    if y in input("Are either of these the hypotenuse?").lower():
        hypotenuse = largest(side1, side2)
        known_side = smallest(side1, side2)
        # a^2 + b^2 = c^2
        # a = sqrt(c^2 - b^2)
        unknown_side = math.sqrt(hypotenuse * hypotenuse - known_side * known_side)
        print(f"The unknown side is {unknown_side} units long!")
    else:
        # a^2 + b^2 = c^2
        # c = sqrt(a^2 + b^2)
        hypotenuse = math.sqrt(side1 * side1 + side2 * side2)
        print(f"The unknown side is {unknown_side} units long!")
        

def identifyTriangle():
    print("Not yet implemented!")

def main():
    print("Welcome to this mathematical program")
    command = ''
    # won't loop again if the user wants to quit 
    while command != 'q':
        bold = "\033[1m"
        end = "\033[0m"
        # bolds characters.
        # What would you like to do?
        # Area | Pythagoras | Triangle Identification | Quit
        command = input(f"What would you like to do?\n{bold}A{end}rea | {bold}P{end}ythogoras | {bold}T{end}riangle Identification | {bold}Q{end}uit\n").lower()
        match command:
            case 'a' | 'area': area(),
            case 'p' | 'pythagoras': pythagoras(),
            case 't' | 'triangle': identifyTriangle(),
            case 'q' | 'quit': print('Goodbye!'),
            case _: print("Invalid command")

if __name__ == "__main__":
    main()
