import java.util.Scanner;
import java.math.*;
public class advancedBitShifting{
	public static void main(String[] args){
		Scanner s1 = new Scanner(System.in);
		BigInteger checker = s1.nextBigInteger();
		float a = System.nanoTime();
		BigInteger originalChecker = checker;
		BigInteger subtract = BigInteger.valueOf(1);
		checker.subtract(subtract);
		checker = checker.or(checker.shiftRight(1));
		checker = checker.or(checker.shiftRight(2));
		checker = checker.or(checker.shiftRight(4));
		checker = checker.or(checker.shiftRight(8));
		checker = checker.or(checker.shiftRight(16));
		checker.add(BigInteger.ONE);     
		System.out.println("Power of two above "+originalChecker+" is : "+checker);
		System.out.println("Time taken : "+(System.nanoTime()-a)/1000000+" milliseconds. "); 
	}
}