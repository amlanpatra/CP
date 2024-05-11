import java.util.Scanner;

public class Solve {

    public static int solve(int n, int m) {
        int dp[] = new int[n + 1];

        for (int i = 1; i < dp.length; i++) {
            if (i < m)
                dp[i] = 1;
            else if (i == m)
                dp[i] = 2;
            else {
                dp[i] = dp[i - 1] + dp[i - m];
            }
        }

        return dp[n];
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        System.out.println(solve(n));
        scn.close();
    }
}
