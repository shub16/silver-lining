import random
import math

def test_case(prime):

	rand = math.floor(prime * random.random())				# Generating random no. less than Prime (supposed)
	while(rand < 3):
		rand = math.floor(prime * random.random())			# random number should be greater than 2
	rand = int(rand)

	highest_odd = prime - 1							# Highest odd factor of (Prime-1)
	pow_of_two = 0								# Coefficient of 2 in prime factors of Prime

	while(highest_odd%2 == 0):
		highest_odd = highest_odd/2
		pow_of_two = pow_of_two + 1

	if ( ((rand**highest_odd) - 1) % prime == 0 ):
		return 1

	for i in range(0,pow_of_two):
		if ( ((rand**((2**i) * highest_odd)) + 1 ) % prime == 0):
			return 1
	return 0

def verify(prime):
	for i in range(0,10):							# !! Set to how many iterations you want.. 
		if (test_case(prime) == 0):
			return 0
	return 1

if __name__ == '__main__':
	prime_or_not = verify(125777)
	if(prime_or_not == 1):
		print "Number is prime"
	else:
		print "Number is not prime"
