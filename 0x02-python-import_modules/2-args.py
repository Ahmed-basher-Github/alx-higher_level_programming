#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    arg_count = len(args)
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
        for arg in args:
            print("{}: {}".format(args.index(arg) + 1, arg))
    else:
        print("{} arguments:".format(arg_count))
        for arg in args:
            print("{}: {}".format(args.index(arg) + 1, arg))
