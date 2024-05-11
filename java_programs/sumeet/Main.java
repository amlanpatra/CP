import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        // Scanner scn = new Scanner(System.in);
        // int n = scn.nextInt();
        System.out.println(solve(3));
    }

    public static int solve(int n) {
        if (n == 0)
            return 1;
        if (n < 0)
            return 0;

        int count = 0;
        for (int i = 0; i < n; i++) {
            count += solve(n - 1); // single
            count += solve(n - 2); // pair
        }

        return count;

    }

}