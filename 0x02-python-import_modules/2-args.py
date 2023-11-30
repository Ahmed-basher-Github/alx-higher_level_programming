#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    arg_count = len(args)
    print("{} arguments:".format(arg_count))
    for arg in args:
        print("{}: {}".format(args.index(arg) + 1, arg))
