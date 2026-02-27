# gets an integer, and allows the user to retry if it's invalid
def getInt(message):
    while True:
        try:
            inputInt = int(input(message + '\n'))
            if inputInt <= 0:
                raise
            else: return inputInt
        except: print("Must be a positive integer")
