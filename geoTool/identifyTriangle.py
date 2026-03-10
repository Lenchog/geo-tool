from geoTool.lib import getInt

# This code is taken from Mr Dwyer's example
 
# This subroutine will accept a valid list of three side lengths of type
#    integer in ascending order
# It will determine and display the classification of the triangle
# The following classifications will be determined:
#  - Isoscelles
#  - Equilateral
#  - Scalene
#  - Right Angled (isoscelles and scalene triangles will be checked for this)
#  - Impossible triangle
def classifyTriangle(sides):

    # Check for impossible triangle
    if sides[0] + sides[1] <= sides[2]:
        print("This is an impossible triangle")

    # Check for equilateral triangle
    elif sides[0] == sides[1] and sides[0] == sides[2]:
        print("This is an equilateral triangle")

    # It will be scalene or isosceles, These can also be right-angled
    else:

        # Check for isosceles
        if (sides[0] == sides[1] or
            sides[0] == sides[2] or
            sides[1] == sides[2]):

            print("This is an isoceles triangle")
        else:
            print("This is a scalene triangle")

        # Check for right angled
        if (sides[0] ** 2) + (sides[1] ** 2) == sides[2] ** 2:
            print("This is also a right-angled triangle")

def getTriangleSides():
    sides = []
    for i in range(3):
        sides[i] = getInt()
    return sides

# This is the controlling module for the identify triangles feature
def identifyTrianglesModule():

    cont = "y"
    while cont == "y":

        sides = getTriangleSides()

        # If the sides are valid, convert to a sorted integer list
        #   and classify them
        # Otherwise print an error
        for i in range(3):
            sides[i] = int(sides[i])
        sides.sort()
        classifyTriangle(sides)

        # Ask if user wants to continue
        print("")
        cont = input(("Enter 'y' to continue with triangle classifications. "
                      "Or any other key to return to the main menu: "))
