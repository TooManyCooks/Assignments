# Programming Assignments

1. Collatz Sequence

2. Stick Conundrum

3. Huffman Encoding

4. Bit Shifting

5. Countdown Game Show


## Collatz Sequence : 
The following iterative sequence is defined for the set of positive integers:

n → n/2 - if n is even.

n → 3n + 1 - if n is odd.

Using this rule and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

The sequence contains 10 terms before it ends on a 1, which ends the sequence.

Find the starting number under 10 million with the longest sequence.

The starting number with the longest sequence is : 
8400511 with a length of 686.

This assignment introduced concepts of optimisation, ie. reusing 
data which has already been calculated, using this snippet of code. 

```java
	sequence[i] = testerCount + sequence[(int)tester];
	if(sequence[i]>count){
		count=(int)sequence[i];
		finishedInt = i;
	}
```



## Stick Conundrum :
Grab a stick. Break it in two. Now randomly break another piece to make three
pieces. What is the probability you can form a triangle?

The answer works out at roughly 19% chance. 

This is determined by the triangle inequality theorem.

![Inequality Theorem](http://images.tutorvista.com/cms/images/67/triangle-inequality.png)

The length of the largest side, must not be greater, than the sum of the remaining sides. 

Demonstrated by some simple python code. 

```python
	if(breakOne>50 or breakTwo>50 or breakThree>50): return 0
	else: return 1
```



## Huffman Coding : 
Derive the huffman codes and compression rate of a piece of text. 

[Huffman Coding](http://en.wikipedia.org/wiki/Huffman_coding)

- Sort data by it's frequency.
- Determine the two smallest frequencies. 
- Combine them.
- Add the combined node back into the tree
- Remove the two smallest. 
- Recursively repeat. 

Demonstrated by this python code.

```python
	counter[twoSmallest[1][0] + twoSmallest[0][0]] = twoSmallest[0][1] + twoSmallest[1][1]
	del counter[twoSmallest[0][0]]
	del counter[twoSmallest[1][0]]
```

To derive the codes, normally a traversal of the Huffman Tree is required. 
But I computer the codes as the program generated the tree. 
I chose the two smallest frequency nodes, as they were combined, the right node
got a 1 appended to it's huffman code, and the left node got a 0 appended. 
For example, a priority queue : 

Y:9, P:7, B:7, A:5, R:4, C:3, Z: 1

After process

Y:9, P:7, B:7, A:5, CZ:4, R:4

C now has a huffman code of 0.

Z now has a huffman code of 1.

This process if repeated until there is only one element remaining it the queue. 

```python
	for i in range(0, len(twoSmallest[0][0])):
		codes[twoSmallest[0][0][i]] = '0'+ str(codes[twoSmallest[0][0][i]]) 
	for j in range(0, len(twoSmallest[1][0])):
		codes[twoSmallest[1][0][j]] = '1'+ str(codes[twoSmallest[1][0][j]]) #
```
