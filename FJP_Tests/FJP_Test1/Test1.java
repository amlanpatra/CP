import java.util.*;

public class Test1 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int num = scn.nextInt();
        scn.close();
        for (int i = 0; i < num; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(ncr(i, j) + "\t");
            }
            System.out.println();
        }
    }

    public static int ncr(int n, int r) {
        return (fact(n) / (fact(r) * fact(n - r)));
    }

    public static int fact(int num) {
        int fact = 1;
        while (num > 0) {
            fact = fact * num;
            num--;
        }
        return fact;
    }
}
