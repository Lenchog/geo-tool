from area import area
from pythagoras import pythagoras
from identifyTriangle import identifyTriangle

def main():
    print("Welcome to this mathematical program")
    bold = "\033[1m"
    end = "\033[0m"
    # bolds characters.
    # What would you like to do?
    # Area | Pythagoras | Triangle Identification | Quit
    command = input(f"What would you like to do?\n{bold}A{end}rea | {bold}P{end}ythogoras | {bold}T{end}riangle Identification | {bold}Q{end}uit\n").lower()
    match command:
        case 'a' | 'area': area(),
        case 'p' | 'pythagoras': pythagoras(),
        case 't' | 'triangle': identifyTriangle(),
        case 'q' | 'quit':
            print('Goodbye!'),
            quit()
        case _: print("Invalid command")

if __name__ == "__main__":
    main()
