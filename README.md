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



