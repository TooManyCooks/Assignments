#!/usr/bin/env python
from collections import defaultdict

maxWord = ''
words = defaultdict(list)
inData = 'AMUSINGMY'

with open('/usr/share/dict/words') as dict_file:
    for word in dict_file:
        if(len(word)>11):
        	words = words
        else:
        	word = word.rstrip('\n').lower()
        	words[''.join(sorted(word))].append(word)

inData = inData.lower()
inData = ''.join(sorted(inData))
newWords = []
print inData

if(len(words[inData])==0):
	for newWord in words:
		temp = newWord
		
		for i in newWord:
			if(i in inData):
				temp = temp.translate(None, i)
		
		if(len(temp)==0):
			newWords.append(newWord)
	
	for word in newWords:
		if(len(word)>len(maxWord) and len(word)<len(inData)):
			maxWord = word
	
	print "The largest word is %s letters long : " % len(maxWord)
	print words[maxWord]

else:
	print "The largest word is nine letters long : "
	print words[inData]


