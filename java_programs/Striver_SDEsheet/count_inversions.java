import java.util.*;
import java.io.*;

public class count_inversions {
    public static void main(String[] args) {

        int arr[] = { 1, 12, 3, 10, 9, 7 };

        int res1[] = mergeSort(arr, 0, arr.length - 1);
        for (int i : res1)
            System.out.print(i + " ");
        System.out.println();
        int res2[] = mergeSort(arr, 0, arr.length - 1);
        for (int i : res2)
            System.out.print(i + " ");

    }

    public static int[] mergeSort(int arr[], int start, int end) {
        if (start == end) {
            int base[] = new int[1];
            base[0] = arr[start];
            return base;
        }
        int mid = (start + end) / 2;
        int left[] = mergeSort(arr, start, mid);
        int right[] = mergeSort(arr, mid + 1, end);
        int res[] = mergeArr(left, right);
        return res;
    }

    public static int[] mergeArr(int arr1[], int arr2[]) {
        if (arr1.length == 0) {
            return arr2;
        }
        if (arr2.length == 0) {
            return arr1;
        }

        int arr[] = new int[arr1.length + arr2.length];

        int i = 0, j = 0, last = 0;
        int count_inversion = 0;
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] <= arr2[j]) {
                arr[last++] = arr1[i++];
            } else {
                arr[last++] = arr2[j++];
            }
        }

        if (i != arr1.length) {
            while (i < arr1.length)
                arr[last++] = arr1[i++];
        } else {
            while (j < arr2.length)
                arr[last++] = arr2[j++];
        }

        return arr;
    }

    public static int[] sort(int arr[], int i, int j) {
        if (i == j) {
            return new int[] { arr[i] };
        }

        int mid = (i + j) / 2;
        int left[] = sort(arr, i, mid);
        int right[] = sort(arr, mid + 1, j);

        int res[] = mergeArr(left, right);
        return res;
    }

}