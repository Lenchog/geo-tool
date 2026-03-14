from geoTool.areaQuiz import areaQuiz
from geoTool.area import area
from geoTool.pythagoras import pythagoras
from geoTool.classifyTriangle import classifyTriangleModule


# main menu, ask for command. Either letters or words in upper or lowercase will work
def main():
    print("Welcome to this mathematical program")
    bold = "\033[1m"
    end = "\033[0m"
    # bolds characters.
    # What would you like to do? Renders as:
    # Area | Pythagoras | Triangle Identification | Quit
    while True:
        command = input(
            f"What would you like to do?\n{bold}A{end}rea | {bold}P{end}ythogoras | {bold}T{end}riangle Identification | {bold}Q{end}uiz | {bold}E{end}xit\n"
        ).lower()

        # look at the first letter of the input to catch a wide variety of cases
        match command[0]:
            case "a":
                area()
            case "p":
                pythagoras()
            case "t":
                classifyTriangleModule()
            case "q":
                areaQuiz()
            case "e":
                print("Goodbye!")
                quit()
            case _:
                print("Invalid command")


if __name__ == "__main__":
    main()
