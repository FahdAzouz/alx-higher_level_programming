#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tot = 0
    i = 0
    for arg in sys.argv:
        tot += int(sys.argv[i])
        i += 1
    print("{:d}".format(tot))
