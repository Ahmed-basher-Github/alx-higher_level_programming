#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    arg_count = len(args)
    if arg_count == 0:
        print("0")
    elif arg_count == 1:
        print(args[0])
    else:
        Sum = 0
        for arg in args:
            Sum = Sum + int(arg)
        print(Sum)
