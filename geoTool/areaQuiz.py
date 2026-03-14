import random
from geoTool.lib import getInt
from geoTool.area import areaTriangle, areaRectangle


# quiz the user on 10 random questions
def areaQuiz():
    print(
        "Welcome to the Area Quiz!\nYou'll be asked 10 questions about the area of a random shape"
    )
    # this variable is incremented when the user answers correctly
    correctAnswers = 0

    questions = 10

    for i in range(1, questions):
        print(f"Question {i}:")
        # we'll use the dimensions no matter the shape (excluding y in the case of square)
        x = random.randrange(1, 100)
        y = random.randrange(1, 100)

        # generate a random shape, mapped to integers
        shape = random.randrange(0, 3)
        match shape:
            # rectangle
            case 0:
                userAnswer = getInt(
                    f"What's the area of a rectangle that's {x} units wide, and {y} units tall?"
                )
                answer = areaRectangle(x, y)
            # triangle
            case 1:
                userAnswer = getInt(
                    f"What's the area of a triangle that's got a base of {x} units, and is {y} units tall?"
                )
                shape = "Triangle"
                answer = areaTriangle(x, y)
            # square
            case 2:
                userAnswer = getInt(
                    f"What's the area of a square with sides {x} units long?"
                )
                answer = areaRectangle(x, x)

        # we mark the user compared to the variable calculated in the match statement
        if userAnswer == answer:
            print("That's right!")
            correctAnswers += 1
        else:
            # we correct the user if they're wrong
            print(f"Incorrect. It's {answer}.")

    # displays the mark
    print(f"You got {correctAnswers} out of {questions}!")
