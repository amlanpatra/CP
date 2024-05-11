import java.util.*;

class Solution {
    // 2.9.22 9:15pm

    public int[] dailyTemperatures(int[] arr) {
        Stack<Integer> s = new Stack<Integer>();
        int res[] = new int[arr.length];
        s.push(0);
        for (int i = 1; i < arr.length; i++) {

            while (!s.isEmpty() && arr[i] > arr[s.peek()]) {

                res[s.peek()] = i - s.peek();
                s.pop();
                s.push(i);

            }
        }
        return res;
    }
}