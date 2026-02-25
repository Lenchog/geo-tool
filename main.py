import math

# TODO figure out how to use multiple files. way too cluttered

def area():
    command = ''
    while command != 'q':
        # TODO reduce repeated code
        command = input("Which shape would you like to calculate the area of?\n")
        if 'circle' in command: 
            print(f"It's {area_circle()} squared units!")
        elif 'square' in command or 'rectangle' in command:
            print(f"It's {area_rectangle()} squared units!")
        elif 'triangle' in command:
            print(f"It's {area_triangle()} squared units!")
        # if the user wants to quit, it's not invalid. however, we don't need to handle the q case
        elif command != 'q':
            print("Invalid command, try again")
        
def area_rectangle():
    x = int(input("How wide is your shape?"))
    y = int(input("How tall is your shape?"))
    return x * y

def area_triangle():
    # catches yes, Yes, Y, y
    # TODO lowercase these 'y's
    if 'y' in input("Do you know both the width and height of this triangle? Y/N\n"):
        # we can utilise the rectangle algorithm
        area = 1/2 * area_rectangle()
    elif 'y' in input("Alright, do you know any angles? Y/N"):
        # TODO I forgot the trig area formula, and I am not connected to the internet
        todo()
    else: print("Sorry, we can't calculate the area then")
    return area

def area_circle():
    # TODO: maybe implement alg for circumference and diameter
    radius = int(input("What is the radius?"))
    # TODO copy and paste pi symbol
    # PIr^2
    return math.pi * radius * radius

def pythogoras():
    side1 = int(input("Give me one side of the triangle\n"))
    if "side" in input("Do you want to use another side, or an angle?\n")
        side2 = int(input("Alright, how long is it?\n"))
        if y in input("Are either of these the hypotenuse?"):
            hypotenuse = largest(side1, side2)
            known_side = smallest(side1, side2)
            # a^2 + b^2 = c^2
            # a = sqrt(c^2 - b^2)
            unknown_side = math.sqrt(hypotenuse * hypotenuse - known_side * known_side))
            print(f"The unknown side is {unknown_side} units long!")
        else:
            # a^2 + b^2 = c^2
            # c = sqrt(a^2 + b^2)
            hypotenuse = math.sqrt(side1 * side1 + side2 * side2)
            print(f"The hypotenuse is {hypotenuse} units long!")
        
def todo():
    print("Not yet implemented!")

print("Welcome to this mathematical program")
command = ''
# won't loop again if the user wants to quit 
while command != 'q':
    # TODO: figure out how to bold so we can do *A*rea to highlight A
    command = input("What would you like to do?\nPress A for area, P for Pythogoras, T for triangle identification, or Q to quit whatever's open\n")
    # TODO: find lowercase function
    match command:
        case 'a': area(),
        case 'p': pythagoras(),
        case 't': todo(),
        case 'q': print('Goodbye!'),
        case _: print("Invalid command")

