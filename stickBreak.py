#!/usr/bin/env python
from random import randint
counter = 0
def stick_divisions():
	breakOne 	= randint(1, 100)
	breakTwo 	= 100 - breakOne
	if(breakOne==50):
		return 0
	else:
		choice = randint(0, 1)
		if(choice == 0):
			breakThree = randint(0, breakOne)
			breakOne -= breakThree
		else:
			breakThree = randint(0, breakTwo)
			breakTwo -= breakThree
		if(breakOne>50 or breakTwo>50 or breakThree>50): return 0
		else: return 1
def get_probability(counter):
	return float(counter / 100000.00)

for i in range(0, 100000):
	counter += stick_divisions()
print counter
probability = get_probability(counter)
print 'Probability is %s' % probability



