#!/usr/bin/env python
import collections
inData = 'The cat sat on the mat'
num_chars = len(inData)
counter = collections.Counter(inData) #Counter to create the "Binary Tree" structure.
codes 	= collections.Counter() #Counter to store the reference and codes. 
unique = list(counter) #Getting the unique characters in the counter. 
print counter
while((len(counter))>1):
	twoSmallest = counter.most_common()[:-2-1:-1] #Command to get the least common elements using regex.
	counter[twoSmallest[1][0] + twoSmallest[0][0]] = twoSmallest[0][1] + twoSmallest[1][1] #Combining the two references and frequencies.
	del counter[twoSmallest[0][0]] #Deleting the two smallest elements. 
	del counter[twoSmallest[1][0]]
	for i in range(0, len(twoSmallest[0][0])):
		codes[twoSmallest[0][0][i]] = '0'+ str(codes[twoSmallest[0][0][i]]) #Appending zeros onto the existing code, if it came from the left side.
	for j in range(0, len(twoSmallest[1][0])):
		codes[twoSmallest[1][0][j]] = '1'+ str(codes[twoSmallest[1][0][j]]) #Appending ones onto the existing code, if it came from the right side.
	print counter
for character in unique: #Looping through every unique character.
	codes[character] = codes[character][:-1] #Trimming the end of each compressed code by one bit.
combined = ''
for letter in inData:
	combined += codes[letter] #Getting a string of all the codes put together, in order to get its length.
newLength = float(len(combined)) #Size of compressed codes.
oldLength = float(num_chars*7) #Size of old codes.
compression = newLength/oldLength #New compression side.
print codes
print 'Compression = %s' % compression