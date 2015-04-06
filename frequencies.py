#!/usr/bin/env python
import collections
counters = []
languages = []

with open('rawencoded.txt') as inData:
	counter = collections.Counter()
	temp = inData.read()
	for x in temp:
		counter[x]+=1
	del counter[' ']

with open('finnish.txt', 'r') as inData:
	finCount = collections.Counter()
	finnish = inData.read()
for x in finnish:
		finCount[x]+=1
del finCount[' ']
counters.append(finCount)
languages.append('Finnish')

with open('german.txt', 'r') as inData:
	gerCount = collections.Counter()
	german = inData.read()
for x in german:
		gerCount[x]+=1
del gerCount[' ']
counters.append(gerCount)
languages.append('German')

with open('french.txt', 'r') as inData:
	frenCount = collections.Counter()
	french = inData.read()
for x in french:
		frenCount[x]+=1
del frenCount[' ']
counters.append(frenCount)
languages.append('French')

with open('iceland.txt', 'r') as inData:
	iceCount = collections.Counter()
	iceland = inData.read()
for x in iceland:
		iceCount[x]+=1
del iceCount[' ']
counters.append(iceCount)
languages.append('Icelandic')

with open('english.txt', 'r') as inData:
	engCount = collections.Counter()
	english = inData.read()
for x in english:
		engCount[x]+=1
del engCount[' ']
counters.append(engCount)
languages.append('English')

with open('polish.txt', 'r') as inData:
	polCount = collections.Counter()
	polish = inData.read()
for x in polish:
		polCount[x]+=1
del polCount[' ']
counters.append(polCount)
languages.append('Polish')

with open('danish.txt', 'r') as inData:
	danCount = collections.Counter()
	danish = inData.read()
for x in danish:
		danCount[x]+=1
del danCount[' ']
counters.append(danCount)
languages.append('Danish')

with open('russian.txt', 'r') as inData:
	russCount = collections.Counter()
	russian = inData.read()
for x in russian:
		russCount[x]+=1
del russCount[' ']
counters.append(russCount)
languages.append('Russian')

with open('swedish.txt', 'r') as inData:
	swedCount = collections.Counter()
	swedish = inData.read()
for x in swedish:
		swedCount[x]+=1
del swedCount[' ']
counters.append(swedCount)
languages.append('Swedish')

with open('spanish.txt', 'r') as inData:
	spanCount = collections.Counter()
	spanish = inData.read()
for x in spanish:
		spanCount[x]+=1
del spanCount[' ']
counters.append(spanCount)
languages.append('Spanish')

print counter
error = 0
minError = 1000000
for i in range(1, len(counters)):
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