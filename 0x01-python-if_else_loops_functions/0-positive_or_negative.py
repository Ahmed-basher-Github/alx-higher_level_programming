#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if(number == 0):
    print(str(number) + " is zero")
elif(number > 0):
    print(str(number) + " is postive")
else:
    print(str(number) + " is negative")
