public class SegmentTree {
    class Node {
        int str, end;
        Node left, right;
        int val;
    }

    Node root;

    Node construct(int nums[], int lo, int hi) {
        if (lo == hi) {
            Node node = new Node();
            node.str = node.end = lo;
            node.left = node.right = null;
            node.val = nums[lo];
            return node;
        }

        Node node = new Node();
        node.str = lo;
        node.end = hi;

        int mid = (lo + hi) / 2;
        node.left = construct(nums, lo, mid);
        node.right = construct(nums, mid + 1, hi);

        node.val += node.left.val + node.right.val;
        return node;
    }

    public static void main(String[] args) {
        node = construct(arr, 0, arr.length - 1);
    }
}
