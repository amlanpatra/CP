import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[][] arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = scn.nextInt();
            }
        }
        diagonal_traverse(arr);
    }

    public static void diagonal_traverse(int[][] arr) {

        int n = arr.length - 1;
        int j = 0, i = n;
        int lmt = (n * 2) - 2;
        for (int k = 1; k <= n; k++) {
            while (i <= n) {
                System.out.println(arr[i][j] + " down i and j is  " + i + " " + j);
                i++;
                j++;
            }
            i--;
            if ((k == n / 2) && (n % 2 == 0)) {
                // i++;
                j++;
            }
            while (j >= 0) {
                System.out.println(arr[i][j] + " up i and j is  " + i + " " + j);
                i--;
                j--;
            }

            j++;

        }
        System.out.println(arr[0][n]);

    }
}