import math
from geoTool.lib import getInt

# we take two sides and whether either is a hypotenuse, and feed it into our maths function
def pythagoras():
    # this is the information we need
    unknown_is_hyp = input("Are you finding the hypotenuse?\n").lower()
    side1 = getInt("Give me one side of the triangle")
    side2 = getInt("Alright, give me another?")

    # we calculate with the below function
    unknown_side = pythag_maths(side1, side2, unknown_is_hyp)
    print(f"The unknown side is {unknown_side} units long!")
    
# use pythagoras' theorem to calculate what's missing
def pythag_maths(side1: int, side2: int, unknown_is_hyp):
     # are we trying to find the hypotenuse, or another side? if so, different formula
    if 'y' in unknown_is_hyp: # one of the sides given are the hypotenuse
        # a^2 + b^2 = c^2
        # c = sqrt(a^2 + b^2)
        return round(math.sqrt(side1 * side1 + side2 * side2), 2)
    else:
        # we know one side is hyp and one isn't. the larger will always be hyp
        hypotenuse = max(side1, side2)
        known_side = min(side1, side2)

        # a^2 + b^2 = c^2
        # a = sqrt(c^2 - b^2)
        return round(math.sqrt(hypotenuse * hypotenuse - known_side * known_side), 2)
