import java.util.*;

public class toast_maxabs_3 {

    public static int median(int[] arr, int start, int end) {
        int length = end - start + 1;
        int median = (arr[start + (length / 2)] + arr[start + ((length - 1) / 2)]) / 2;
        return median;
    }

    public static int abs_sum(int[] arr, int start, int end, int median) {
        int res = 0;
        for (int i = start; i <= end; i++) {
            res += Math.abs(arr[i] - median);
        }
        return res;
    }

    public static int soln(int[] arr) {
        Arrays.sort(arr);
        int sum = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length - 1; i++) {
            int median1 = median(arr, 0, i);
            int median2 = median(arr, i + 1, arr.length - 1);
            int sum1 = abs_sum(arr, 0, i, median1);
            int sum2 = abs_sum(arr, i + 1, arr.length - 1, median2);
            sum = (sum1 + sum2) < sum ? (sum1 + sum2) : sum;
        }
        return sum;
    }

    public static void main(String[] args) {

        int arr1[] = { 78, 97, 23, 6, 51, 52, 28, 60, 33, 1, 100 };
        int arr2[] = { 95, 15, 14, 8, 58, 30, 49, 32, 68, 71, 100, 82, 65, 40, 7, 57, 65, 75, 51, 80, 97, 87, 36, 45,
                12,
                44, 56, 27, 55, 40, 83, 30, 36, 21, 72, 75 };

        System.out.println(soln(arr1));
        System.out.println(soln(arr2));

    }
}
