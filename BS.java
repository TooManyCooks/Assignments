import java.math.BigInteger;
import java.util.HashMap;
import java.util.Scanner;

// Comments come directly from the algorithm
// on http://en.wikipedia.org/wiki/Baby-step_giant-step

public class BS{
	
	// Variables for Rob's method.
	private static final BigInteger valueOfTwo = BigInteger.valueOf(2L);
	private static final int ONCE = 1;
	
	public static void main(String[] args){
		Scanner s1 = new Scanner(System.in);
		BigInteger p1 = new BigInteger("24852977"); 
		BigInteger g1 = new BigInteger("2744");
		BigInteger y1 = new BigInteger("8414508"); 
		BigInteger c11 = new BigInteger("15268076"); 
		BigInteger c21 = new BigInteger("743675"); 

		BigInteger p2 = new BigInteger("85754635859");  
		BigInteger g2 = new BigInteger("181673");
		BigInteger y2 = new BigInteger("34109547043"); 
		BigInteger c12 = new BigInteger("26398053246");
		BigInteger c22 = new BigInteger("72955071594"); 

		System.out.println("Press S for normal solution, press B for bonus solution.");
		String selector = new String();
		selector = s1.next();

		if(selector.compareTo("S")== 0 ) scrubQuestion(p1, g1, y1, c11, c21);
		else if(selector.compareTo("B")== 0 ) bonusQuestion(p2, g2, y2, c12, c22);
		
	}

	public static void scrubQuestion(BigInteger p, BigInteger g, BigInteger y, BigInteger c1, BigInteger c2){
		BigInteger privateKey = getPrivateKey(p, g, y);
		System.out.println("Private Key = "+privateKey);
		BigInteger message;
		message = c1.modPow(p.subtract(BigInteger.ONE).subtract(privateKey), p);
		message = message.multiply(c2).mod(p);
		System.out.println("Message = "+message);
	}

	public static void bonusQuestion(BigInteger p, BigInteger g, BigInteger y, BigInteger c1, BigInteger c2){
		BigInteger privateKey = getPrivateKey(p, g, y);
		System.out.println("Private Key = "+privateKey);
		BigInteger message;
		message = c1.modPow(p.subtract(BigInteger.ONE).subtract(privateKey), p);
		message = message.multiply(c2).mod(p);
		System.out.println("Message = "+message);
	}
	public static BigInteger getPrivateKey(BigInteger p, BigInteger g , BigInteger y){
		
		// m = Ceiling(sqrt(n))
		BigInteger squareRootP = sqrtN(p);

		// Creating a table as a hashmap.
		HashMap<BigInteger, BigInteger> values = new HashMap<BigInteger, BigInteger>();

		// For all j where 0 <= j < m:
		for(BigInteger i = BigInteger.ZERO; i.compareTo(squareRootP) != 1; i = i.add(BigInteger.ONE)){
			// Compute aj and store the pair (j, aj) in a table.
			values.put(g.modPow(i, p), i);
		}

		// Compute a^-m
		BigInteger c = (g.modPow(squareRootP.negate(), p));

		// Initial value of privateKey is 0.
		BigInteger privateKey = BigInteger.valueOf(0L);

		// Preserving the y value.
		BigInteger t = y;

		// For i = 0 to (m-1)
		for(BigInteger i = BigInteger.ZERO; i.compareTo(squareRootP) != 0; i = i.add(BigInteger.ONE)){
			
			// Check to see if y is the second component (aj) of any pair in the table.
			if(values.containsKey(t))
			{
				
				// If so, return im + j
				BigInteger computedKey = values.get(t);
				privateKey = (squareRootP.multiply(i)).add(computedKey);
				return privateKey;

			}

			// If not, y = y * a^-m (pre-computed)
			else t = (t.multiply(c)).mod(p);
		}
		
		return privateKey;
	}

	// Rob's big int square root method. 
	private static BigInteger sqrtN(BigInteger inNumber) {
		int c = 0;
		BigInteger n0 = valueOfTwo.pow(inNumber.bitLength() >> 1);
		BigInteger np = inNumber;
		do{
		    n0 = n0.add(inNumber.divide(n0)).shiftRight(ONCE);
		    c = np.compareTo(n0);
		    np = n0;
		}while(c != 0);
		return n0;
	}
}
