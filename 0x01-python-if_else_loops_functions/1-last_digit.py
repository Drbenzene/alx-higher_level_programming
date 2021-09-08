#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit == 0:
        print("Last digit of {} is {} and is 0".format(number, last_digit))
elif number < 0:
        neg_number = number * -1
        last_digit = neg_number % 10
        print("Last digit of {} is -{} and is less than 6 and not 0".format(number, last_digit))

elif number > 0:
        if number > 6:
                print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))
else:
        print("Last digit of {} is {} and is greater than 5".format(number, n))
