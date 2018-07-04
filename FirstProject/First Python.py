import sys
import math

def pythag(a, b):
    a_squared = math.pow(a, 2)
    b_squared = math.pow(b, 2)

    added = a_squared + b_squared

    return math.sqrt(added)



def main():
    UserInput = sys.argv[1]
    if (UserInput == "add"):
        print(int(sys.argv[2]) + int(sys.argv[3]))

    if (UserInput == "sub"):
        print(int(sys.argv[2]) - int(sys.argv[3]))

    if(UserInput == "countto"):
        x = int(sys.argv[2])

        for i in range(x+1):
            print(i)

    if(UserInput == "hypot"):
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(pythag(x,y))

    if(UserInput == "repeat"):
    x = sys.argv[2]
    y = int(sys.argv[3])
    for i in range(y):
    print(x)

    if(UserInput == "power"):
    print(int(sys.argv[2]) ** int(sys.argv[3]))



if __name__ == "__main__":
    main()