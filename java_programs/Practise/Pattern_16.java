import java.util.*;

public class Pattern_16 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        scn.close();
        int nstars = 1;
        int nspaces = (2 * n) - 3;

        for (int i = 1; i <= n; i++) {
            int start = 1;
            for (int j = 1; j <= nstars; j++) {
                System.out.print(start + "\t");
                start++;
            }
            for (int j = 1; j <= nspaces; j++) {
                if (j <= nspaces / 2) {
                    start++;
                } else {
                    start--;
                }
                System.out.print("\t");
            }
            if (nspaces < 1) {
                nstars--;
                start -= 2;
            }
            for (int j = 1; j <= nstars; j++) {
                System.out.print(start + "\t");
                start--;
            }
            System.out.println();

            nstars++;
            nspaces -= 2;
        }
    }
}
