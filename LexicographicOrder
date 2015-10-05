public class lexicographicOrder{

    public static void main(String[] args){
        
        int N = 25;
        
        for(int i = 1; i <= 9; i++){
            if(i < N){
                System.out.println(i);
            }

            if(i*10 < N){
                lexicographic(i*10, N, 10);
            }
        }
    }
    
    static void lexicographic(int power, int N, int searchSpace){
        for(int j = power; j < power+searchSpace; j++){
            if(j <= N){
                System.out.println(j);
            }
        }
        if(power*10 < N){
            lexicographic(power*10, N, searchSpace*10);
        }
    }
}
