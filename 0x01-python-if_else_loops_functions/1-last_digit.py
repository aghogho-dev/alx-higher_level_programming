#!/usr/bin/python3
import random
number = random.randint(-10_000, 10_000)

if 0 <= number < 10:
    last_number = number % 10

elif 10 <= number < 100:
    last_number = (number % 100) % 10

elif 100 <= number < 1000:
    last_number = ((number % 1000) % 100) % 10

elif 1000 <= number < 10_000:
    last_number = (((number % 10_000) % 1000) % 100) % 10

elif -10 < number < 0:
    last_number = number % -10

elif -100 < number <= -10:
    last_number = (number % -100) % -10

elif -1000 < number <= -100:
    last_number = ((number % -1000) % -100) % -10

elif -10000 < number < -1000:
    last_number = (((number % -10_000) % -1000) % -100) % -10

else:
    last_number = 0

if last_number == 0:
    print(f"Last digit of {number} is {last_number} and is 0")

elif last_number > 5:
    print(f"Last digit of {number} is {last_number} and is greater than 5")

elif last_number < 6:
    print(f"Last digit of {number} is {last_number} and is less than 6 and not 0")
