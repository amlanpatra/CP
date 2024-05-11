class NumArray {
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

    public NumArray(int[] nums) {
        root = construct(nums, 0, nums.length - 1);
    }

    public void update(Node node, int idx, int val) {
        if (node.str == node.end) {
            node.val = val;
        }else{
            update(node.right,)
        }
    }

    int query(Node node, int qs, int qe) {
        if (qs > node.end || qe < node.str) {
            return 0;
        } else if (node.str >= qs && node.end <= qe) {
            return node.val;
        } else {
            int lval = query(node.left, qs, qe);
            int rval = query(node.right, qs, qe);
            return lval + rval;
        }
    }

    public int sumRange(int left, int right) {
        return query(root, left, right);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */
