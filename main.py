def todo():
    print("Not yet implemented!")

print("Welcome to this mathematical program")
command = ''
# won't loop again if the user wants to quit 
while command != 'q':
    command = input("What would you like to do?\nPress A for area, P for Pythogoras, T for triangle identification, or Q to quit whatever's open\n")
    # TODO: find lowercase function
    match command:
        case 'a': todo(),
        case 'p': todo(),
        case 't': todo(),
        case 'q': print('Goodbye!'),
        case _: print("Invalid command")

