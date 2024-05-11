#define max 1000
#include <stdio.h>
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l)
    {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x)
            return mid;
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);
        return binarySearch(arr, mid + 1, r, x);
    }
    return -1;
}
int main(void)
{
    int arr[max] = {0}, cases, i = 0, key;
    printf("Enter how many numbers you want to enter : ");
    scanf("%d", &cases);
    printf("\nEnter the numbers : \n");
    while (cases--)
        scanf("%d", &arr[i++]);

    printf("Enter the number you want to search : ");
    scanf("%d", &key);
    int result = binarySearch(arr, 0, i - 1, key);
    (result == -1) ? printf("Element is not present in array\n")
                   : printf("Element is present at position %d\n",
                            result + 1);
}