#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
if x > 5:
    print("last digit of {} is {} and great than 5 ".format(number,x))
elif x == 0:
    print("last digit of {} is {} and is 0 ".format(number,x))
else:
    print("last digit of {} is {} and is less than 6 and not 0 ".format(number,x))
