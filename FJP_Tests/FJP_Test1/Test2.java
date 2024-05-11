import java.util.*;

public class Test2 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                char x = (char) (i + 64);
                if ((j > 1) && (j < i))
                    System.out.print("*");
                else
                    System.out.print(x);
            }
            System.out.println();
        }
        System.out.println();
    }
}
