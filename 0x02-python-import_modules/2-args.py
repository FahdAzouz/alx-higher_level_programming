#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))

    elif i >= 1:
        if i == 1:
            print("{} argument:".format(i))
        else:
            print("{} arguments:".format(i))
        i = 1
        for arg in sys.argv:
            print("{}: {}".format(i, arg))
            i += 1
