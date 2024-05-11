import java.util.*;

public class target_sum_triplet {

    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = scn.nextInt();
        }
        int tar = scn.nextInt();
        Arrays.sort(arr);

        int left = 0;
        int right = arr.length - 1;
        int target = tar;
        System.out.println("\nOutput is : ");

        for (int i = 0; i < arr.length; i++) {
            // for (int i = 0; i <= arr.length / 2; i++) {
            left = i + 1;
            right = arr.length - 1;
            target = tar - arr[i];

            while (left < right) {
                if ((arr[left] + arr[right]) > target) {
                    right--;
                } else if ((arr[left] + arr[right]) < target) {
                    left++;
                } else {
                    System.out.println(arr[i] + "," + arr[left] + "," + arr[right]);
                    left++;
                    right--;
                }
            }
        }
    }

}
// 11 1 9 6 4 8 3 12 14 24 10 15 25