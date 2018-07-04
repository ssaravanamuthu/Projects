import sys

def main():
    UserInput = sys.argv[1]

    if (UserInput == "Sirish"):
        print("Hello Sirish")

    if (UserInput == "Classified"):
         print("This message is classified and can only be viewed with another important word!")

    if (UserInput == "Jamestown"):
        print("The main ship is still up and moving about. It is up to you to take it down before ultimate destruction occurs. We have faith in you. Good Luck!")

    if (UserInput == "Mission"):
        print("Your mission now is to get control of one of the navy's destroyers and head out to destroy the main ship. If you fail the mission then you will be killed. Good Luck!")

if __name__ == "__main__":
    main()
