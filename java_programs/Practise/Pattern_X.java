import java.util.*;

public class Pattern_X {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int num = scn.nextInt();
        int fsp = 0;
        int ssp = num - 1;

        for (int i = 0; i < num; i++) {
            for (int j = 0; j < fsp; j++) {
                System.out.print("\t");
            }
            System.out.print("*");
            for (int j = 0; j < ssp; j++) {
                System.out.print("\t");
            }
            if (i != num / 2)
                System.out.println("*");
            else
                System.out.println();
            if (i < num / 2) {
                fsp++;
                ssp = ssp - 2;
            } else {
                fsp--;
                ssp = ssp + 2;
            }
        }
        scn.close();
    }
}