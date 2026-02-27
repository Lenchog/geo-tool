import math
from lib import getInt

# we take two sides and whether either is a hypotenuse,
# then use pythagoras' theorem to calculate what's missing
def pythagoras():
    side1 = getInt("Give me one side of the triangle")
    side2 = getInt("Alright, give me another?")
    # are we trying to find the hypotenuse, or another side? if so, different formula
    if 'y' in input("Are either of these the hypotenuse?\n").lower():
        # TODO find function to do this quicker
        if side1 > side2:
            hypotenuse = side1
            known_side= side2
        else:
            hypotenuse = side2
            known_side = side1
        # a^2 + b^2 = c^2
        # a = sqrt(c^2 - b^2)
        unknown_side = math.sqrt(hypotenuse * hypotenuse - known_side * known_side)
        print(f"The unknown side is {unknown_side} units long!")
    else:
        # a^2 + b^2 = c^2
        # c = sqrt(a^2 + b^2)
        hypotenuse = math.sqrt(side1 * side1 + side2 * side2)
        print(f"The unknown side is {unknown_side} units long!")
        
