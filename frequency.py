#!/usr/bin/env python
import collections
counters = []
languages = ['Finnish', 'English', 'Polish', 'Russian', 'German']

with open('rawencoded.txt') as inData:
	counter = collections.Counter()
	temp = inData.read()
	for x in temp:
		counter[x]+=1
	del counter[' ']

finCount = collections.Counter({'a' : 22.22, 'i' : 10.82, 'n' : 8.83, 't' : 8.75, 'e' : 7.95, 's' : 7.86, 'l' : 5.76, 'o' : 5.61})
engCount = collections.Counter({'e' : 12.7, 't' : 9.05, 'e' : 8.16, 'o' : 7.50, 'i' : 6.96, 'n' : 6.74, 's' : 6.32, 'h' : 6.09})
polCount = collections.Counter({'a' : 10.85, 'i' : 8.32, 'e' : 7.35, 'o' : 6.66, 'n' : 6.23, 'w' : 5.81, 'r' : 5.24, 's' : 5.22})
russCount = collections.Counter({'o': 10.61, 'e' : 8.21, 'a' : 8.04, 'n' : 7.98, 'h' : 6.72, 't' : 5.83, 'c' : 5.71, 'p' : 5.38})
gerCount = collections.Counter({'e' : 16.3, 'n' : 9.77, 's' : 7.27, 'r' : 7, 'i' : 6.55, 'a' : 6.51, 't' : 6.15, 'd' : 5.07})

counters.append(finCount), counters.append(engCount), counters.append(polCount), counters.append(russCount), counters.append(gerCount)

error = 0
minError = 1000000
for i in range(0, len(counters)):
	temp1 = dict(counters[i].most_common(5))
	temp2 = dict(counter.most_common(5))
	for j in range(0, len(temp1)):
		error += abs(temp1.items()[j][1] - temp2.items()[j][1])
	print error
	if error <= minError:
		minError = error
		minCounter = counters[i]
		mini = i
	error = 0
print languages[mini]

points = []
x,y = [], []
names = []
with open('tspPoints.txt', "r") as pointsFile:
	temp = pointsFile.read()
	for l in temp:
		row = temp.split(',')
   		names.append(row[0])
   		x.append(row[1])
   		y.append(row[2])
print x 
print y

