import java.util.*;
public class toast_zsec_iter_new {
    public static void main(String[] args) {

        System.out.println(z_sec(664, 464, 166));
        System.out.println(z_sec(648, 938, 39));
        System.out.println(z_sec(416, 600, 201));
        System.out.println(z_sec(966, 264, 357));
        System.out.println(z_sec(180, 294, 143));
        System.out.println(z_sec(752920, 410368, 402885));
        System.out.println(z_sec(664744, 449680, 564517));
        System.out.println(z_sec(120442, 477795, 567387));
        System.out.println(z_sec(194696, 596652, 522681));
        System.out.println(z_sec(907240, 461884, 979233541));

    }

    public static int z_sec(int p, int q, int n) {

        if (n >= 1000) {
            return solve(p, q, n);
        }

        int sum = 0, i = 0;
        while (i != n + 1) {
            if (i == 0) {
                sum = 2;
            } else {
                sum = (p * Integer.bitCount(sum) + q);
            }
            i++;
        }
        return Integer.bitCount(sum);
    }

    public static int[] get_series(int p, int q) {
        int arr[] = new int[20];
        for (int i = 0; i < 20; i++) {
            arr[i] = (z_sec(p, q, i));
        }
        return arr;
    }

    public static ArrayList<Integer> find_repeat_index(int arr[]) {
        // returns arraylist with [index of first_repeat_index, all the repeating
        // characters]

        HashSet<Integer> set = new HashSet<>();
        int start = 0;
        int end = 0;
        for (int i = 0; i < arr.length; i++) {
            if (set.contains(arr[i])) {
                end = i;
                break;
            } else {
                set.add(arr[i]);
            }
        }

        for (int i = 0; i < end; i++) {
            if (arr[i] == arr[end]) {
                start = i;
                break;
            }
        }

        ArrayList<Integer> al = new ArrayList<>();
        al.add(start);

        for (int i = start; i < end; i++) {
            al.add(arr[i]);
        }
        return al;
    }

    public static int solve(int p, int q, int n) {
        // arr[start, repeating values]
        // start is the new 0th index
        ArrayList<Integer> al = find_repeat_index(get_series(p, q));

        n = n - al.get(0);
        int res = n % (al.size() - 1);
        return al.get(res + 1);
    }
}
