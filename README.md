# Programming Assignments
.. Collatz Sequence
.. Stick Conundrum
.. Huffman Encoding
.. Bit Shifting
.. Countdown Game Show

## Collatz Sequence : 
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using this rule and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
The sequence contains 10 terms before it ends on a 1, which ends the sequence.
Find the starting number under 10 million with the longest sequence.

The starting number with the longest sequence is : 
8400511 with a length of 686.

This assignment introduced concepts of optimisation, ie reusing 
data which has already been calculated, using this snippet of code. 
'''java
      //Editing sequence so that the count you just got is added to the values you already have.
			sequence[i] = testerCount + sequence[(int)tester];
			//Comparing if the array sequence is larger than a previous instance, in order to get the largest.
			if(sequence[i]>count){
				count=(int)sequence[i];
				finishedInt = i;
			}
'''
