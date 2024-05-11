class mediansort {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/1701107/Java-Binary-Search-Explained
        int m = nums1.length;
        int n = nums2.length;
        int m1 = (m + n + 1) / 2;
        int m2 = (m + n + 2) / 2;

        int median1 = getKthElementFromMergedArray(nums1, nums2, m1, 0, 0);
        int median2 = getKthElementFromMergedArray(nums1, nums2, m2, 0, 0);

        return (median1 + median2) / 2.0;
    }

    public static int getKthElementFromMergedArray(int nums1[], int nums2[], int k, int s1, int s2) {

    }

}