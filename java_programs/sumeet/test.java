import java.util.ArrayList;

public class test {
    public static void main(String[] args) {

    }
}

class Solution {
    public boolean isPalindrome(ListNode head) {
        String s = "";

        ListNode temp = head;

        s += Integer.toString(temp.val);
        while (temp.next != null) {
            temp = temp.next;
            s += temp.val;
        }

        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) == s.charAt(right)) {
                left++;
                right--;
            } else
                return false;
        }
        return true;
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}