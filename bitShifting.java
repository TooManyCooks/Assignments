import java.util.Scanner;
import java.math.*;
public class bitShifting{
	public static void main(String[] args){
		Scanner s1 = new Scanner(System.in);
		long checker = s1.nextLong();
		long originalChecker = checker;

		float a = System.nanoTime();

		if((checker > 0) && ((checker & (checker-1)) == 0)==true){
			System.out.println("Power of two above "+checker+" is "+checker);
		}

		else if((checker > 0) && ((checker & (checker-1)) == 0)==false) {
			String check = Long.toBinaryString(originalChecker);
			int shift = check.length();
			checker = checker >> shift-1;
			checker = checker << shift;
			System.out.println("Power of two above "+originalChecker+" is "+checker);
		}

		else{
			System.out.println("Power of two above "+checker+" is "+0);
		}

		System.out.println("Time taken : "+(System.nanoTime()-a)/1000000+" milliseconds.");
	}
}