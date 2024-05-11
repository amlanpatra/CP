import java.util.*;

public class Pattern_M {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int num = scn.nextInt();
        for (int i = 1; i <= num; i++) {
            for (int j = 1; j <= num; j++) {
                if (i > 1 && i <= num) {
                    if (j == 1 || j == num)
                        System.out.print("*");
                }
                if (i == j || i + j == num + 1) {
                    if (i <= (num / 2) + 1)
                        System.out.print("*\t");
                    else
                        System.out.print("\t");
                } else
                    System.out.print("\t");
            }
            System.out.println();
        }
    }
}
