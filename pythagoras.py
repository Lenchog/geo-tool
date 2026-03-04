import math
from lib import getInt

# we take two sides and whether either is a hypotenuse,
# then use pythagoras' theorem to calculate what's missing
def pythagoras():
    side1 = getInt("Give me one side of the triangle")
    side2 = getInt("Alright, give me another?")
    unknown_is_hyp = input("Are you finding the hypotenuse?\n").lower()
    unknown_side = pythag_maths(side1, side2, unknown_is_hyp)
    print(f"The unknown side is {unknown_side} units long!")
    
def pythag_maths(side1: int, side2: int, unknown_is_hyp):
     # are we trying to find the hypotenuse, or another side? if so, different formula
    if 'n' in unknown_is_hyp: # one of the sides given are the hypotenuse
        # TODO find function to do this quicker
        if side1 > side2:
            hypotenuse = side1
            known_side= side2
        else:
            hypotenuse = side2
            known_side = side1
        # a^2 + b^2 = c^2
        # a = sqrt(c^2 - b^2)
        return math.sqrt(hypotenuse * hypotenuse - known_side * known_side)
    else:
        # a^2 + b^2 = c^2
        # c = sqrt(a^2 + b^2)
        return math.sqrt(side1 * side1 + side2 * side2)
