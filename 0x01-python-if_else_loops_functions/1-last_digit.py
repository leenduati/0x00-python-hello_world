#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg_num = 0
sol = 0

# initialize sol(to accept the last num) and neg_num(to cater for negative numbers)

# a function to fulfill conditions necessary
def check_num(n):
	if n > 5:
		print(f'Last digit of {number} is {n} and is greater than 5')
	elif n == 0:
		print(f'Last digit of {number} is {n} and is 0')
	else:
		print(f'Last digit of {number} is {n} and is less than 6 and not 0')


# call the function
if number < 0:
	neg_num = number * -1
	sol = neg_num % 10
	check_num(-sol)
else:
	sol = number % 10
	check_num(sol)
