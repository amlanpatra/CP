import java.util.*;

public class Jd {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number");
        int n = sc.nextInt();
        int c = 0;
        for (int i = 2; i <= (n / 2); i++) {
            if (n % i == 0)
                c = c + 1;
        }
        if (c == 0)
            System.out.println("Given number is prime number");
        else
            System.out.println("Given number is not prime number");
    }
}

// int arr[] = { 12, -2, 3, -4, -10, 6 };
// int sums[] = new int[100];
// int max, sum;

// for (int i = 0; i < arr.length; i++) {
// sum = 0;
// max = 0;
// for (int j = i; j < arr.length; j++) {
// sum += arr[j];
// max = sum > max ? sum : max;
// }
// sums[i] = max;
// }
// max = sums[0];
// for (int i = 0; i < arr.length; i++) {
// // System.out.println(sums[i]);
// max = sums[i] > max ? sums[i] : max;
// }

// System.out.println("The maximum sum is " + max);

// optimised approach for maximum subarray sum

// int max = arr[0], sum = 0;
// for (int i = 0; i < arr.length; i++) {
// sum += arr[i];
// max = sum > max ? sum : max;
// sum = sum < 0 ? 0 : sum;
// }
// System.out.println(max);