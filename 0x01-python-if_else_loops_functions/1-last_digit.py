#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    num = number % 10
else:
    num = ((number * -1) % 10) * -1
print(f'Last digit of {number} is {num} and is', end=' ')
if num > 5:
    print('greater than 5')
elif num == 0:
    print('0')
else:
    print('less than 6 and not 0')
