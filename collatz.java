public class collatz
{
	public static void main(String args[]) {
		long time = System.currentTimeMillis();
		long[] sequence = new long[10000001];
		int finishedInt = 0;
		int i = 0;
		int count = 0;
		long tester = 1;
		int testerCount = 1;
		//Initialising all instances of array sequence. 
		for(i = 1 ; i<sequence.length ; i++){
			sequence[i]=i;
		}
		//Begins looping a constant variable i.
		for(i = 2 ; i < 10000000 ; i++){
			testerCount = 0;
			tester = i;
			//Loops through all possible numbers to be tested and tests them.
			while(tester != 1 && tester >= i){
				//Testing if it's even, right shifting is true.
				if(tester%2==0) tester=(tester>>1);
				//Testing if it's odd
				else tester=(tester*3)+1;
				
				testerCount++;
			}
			//Editing sequence so that the count you just got is added to the values you already have.
			sequence[i] = testerCount + sequence[(int)tester];
			//Comparing if the array sequence is larger than a previous instance, in order to get the largest.
			if(sequence[i]>count){
				count=(int)sequence[i];
				finishedInt = i;
			}
		}
		//Printing out the starting value of the longest sequence and how many integers are in it's length.
		System.out.println("The sequence starting at "+finishedInt+" has a length of "+count);
		System.out.println(System.currentTimeMillis()-time+"ms, GOTTA GO FAST!");
	}
}