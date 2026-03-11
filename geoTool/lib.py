# gets an integer, and allows the user to retry if it's invalid
def getInt(message):
    # we use a while loop to continue until the user enters something valid
    while True:
        try:
            # we use the validateInt() function, plus input with the message sent.
            # a newline is also added, so it's consistent with every input in the program
            return validateInt(input(message + '\n'))
        except: print("Must be a positive integer")

# this function returns errors if it's not right.
# that crashes by default, but is caught by the `try` in getInt()
# Should be an integer 
def validateInt(input):
    inputInt = int(input)
    # must be positive
    if inputInt <= 0:
        raise Exception("Number should be larger than 0")
    return inputInt
