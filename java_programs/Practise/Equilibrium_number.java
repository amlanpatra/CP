class Equilibrium_number {
    public static void main(String[] args) {
        // equilibrium number
        int arr[] = { 12, -13, 14, 4, 8, 2, 2, 1 };
        int sum = 0, left_sum = 0, i;
        for (i = 0; i < arr.length; i++)
            sum += arr[i];

        for (i = 0; i < arr.length; i++) {
            left_sum += arr[i];
            if (left_sum == sum) {
                break;
            }
            sum -= arr[i];
        }
        System.out.println("Equivalent number is " + arr[i] + " at position arr[" + i + "]");
    }
}