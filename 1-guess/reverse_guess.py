# Think of a number between 0 and 99. Then write a python program
# to guess the number you have thought of
import random


def verify_guess(val):

	print("I am guessing {}".format(val)+" is it correct?")
	response = None
	while response is None:
		response = raw_input("Enter your response: ")
	return response

number = random.randint(0, 99)
lowerbound = 0
higherbound = 99


res = verify_guess(number)
while res != 'Y':
	prev = number
	if res == 'H':
		lowerbound = number
		number = number+((higherbound-number)//2)
	elif res == 'L':
		higherbound = number
		number = number-((number-lowerbound)//2)
	res = verify_guess(number)

print("I got it, it was {}".format(number))

