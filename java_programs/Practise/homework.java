import java.util.*;

public class homework {
    public static void main(String args[]) {
        Scanner scn = new Scanner(System.in);
        int k = scn.nextInt();

        for (int i = 0; i < k; i++) {
            int num = scn.nextInt();
            boolean isPrime = true;
            int start = 2;
            while (start * start <= num) {
                if (num % start == 0) {
                    isPrime = false;
                    break;
                }
                start++;
            }
            if (isPrime == true)
                System.out.println(num + " is Prime");
            else
                System.out.println(num + " is not prime");
        }
        scn.close();
    }
}
