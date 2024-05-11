import java.util.*;

class Primality_Test {
    public static void main(String args[]) {
        // Scanner scn = new Scanner(System.in);
        // int n = scn.nextInt();
        int n = 4;
        System.out.println(Prime(n));
    }


    public static boolean Prime(int n) {
        boolean isPrime = true;
        for (int i = 2; i <= n / i ; i++) {
            if (n % i == 0) {
                isPrime = false;
                return isPrime;
            }
        }
        return isPrime;
    }
}
