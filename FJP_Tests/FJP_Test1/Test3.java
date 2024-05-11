import java.util.*;

public class Test3 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        scn.close();
        int val = 1, mult = 0;
        for (int i = 1; i <= n; i++) {

            for (int j = 1; j <= n; j++) {
                if (((i > 1) && (i < n)) && ((j > 1) && (j < n)))
                    System.out.print("*\t");
                else
                    System.out.print(val + "\t");
                val++;
            }
            System.out.println();

            if (n % 2 != 0) {
                if (i <= (n / 2)) {
                    mult += 2;
                } else if (i == (n / 2 + 1)) {
                    mult = n - 2;
                } else {
                    mult -= 2;
                }
            } else {
                if (i < (n / 2)) {
                    mult += 2;
                } else if (i == n / 2) {
                    mult = n - 1;
                } else {
                    mult -= 2;
                }
            }
            val = n * mult + 1;
        }

    }
}