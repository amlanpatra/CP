import java.util.*;

public class sieve_prime_no {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int num = scn.nextInt();

        boolean[] sieve = new boolean[num];

        for (int i = 2; i * i < sieve.length; i++) {
            if (sieve[i] == false) {
                for (int j = 2; i * j < sieve.length; j++) {
                    sieve[i * j] = true;
                }
            }
        }
        for (int k = 2; k < sieve.length; k++) {
            if (sieve[k] == false) {
                System.out.println(k);
            }
        }
    }
}
