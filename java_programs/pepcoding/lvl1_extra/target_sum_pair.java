import java.util.*;

public class target_sum_pair {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = scn.nextInt();
        }
        int target = scn.nextInt();
        Arrays.sort(arr);

        int left = 0;
        int right = arr.length - 1;

        // System.out.println("\nOutput is : ");
        while (left < right) {
            if ((arr[left] + arr[right]) > target) {
                right--;
            } else if ((arr[left] + arr[right]) < target) {
                left++;
            } else {
                System.out.println(arr[left] + "," + arr[right]);
                left++;
                right--;
            }
        }
    }

}
