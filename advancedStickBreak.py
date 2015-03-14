#!/usr/bin/env python
import random
from random import randint
counter = 0.0
def get_partitions(amount):
	newSelect = 0
	breaks = [100.00]
	for i in range(1, amount):
		select = randint(0, len(breaks)-1)
		oldBreak = breaks[select]
		newBreak = random.uniform(0.0, oldBreak)
		oldBreak -= newBreak
		breaks.append(newBreak)
		breaks[select] = oldBreak
	return breaks
def can_triangle(breaks):
	length = len(breaks)
	breaks.sort()
	for i in range(0, length):
		for j in range(1, length-1):
			if(breaks[i] + breaks[j] >= breaks[j+1]):
				return False
			else:
				print "Breaks : {0} \ncounter : {1}".format(breaks, counter)
				return True
				break
brokenTimes = input("How many times do you break a stick? : ")
for i in range(0, 10000):
	breaks = get_partitions(brokenTimes)
	if(can_triangle(breaks)==True):
		counter += 1
	
probability = 1-(counter/10000.00)
print probability

	



