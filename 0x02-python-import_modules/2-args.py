#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1

    if i == 0:
        print("{} arguments.".format(i))

    elif i >= 1:
        if i == 1:
            print("{} argument:".format(i))
        else:
            print("{} arguments:".format(i))

        for arg in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
            i += 1
