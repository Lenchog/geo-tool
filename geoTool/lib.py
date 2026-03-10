# gets an integer, and allows the user to retry if it's invalid
def getInt(message):
    while True:
        try:
            return validateInt(input(message + '\n'))
        except: print("Must be a positive integer")

# Should be an integer 
def validateInt(input):
    inputInt = int(input)
    if inputInt <= 0:
        raise Exception("Number should be larger than 0")
    return inputInt
