#include <stdio.h>

#define max 100

int a[max] = {0};
int b[10];

void merging(int low, int mid, int high)
{
    int l1, l2, i;

    for (l1 = low, l2 = mid + 1, i = low; l1 <= mid && l2 <= high; i++)
    {
        if (a[l1] <= a[l2])
            b[i] = a[l1++];
        else
            b[i] = a[l2++];
    }

    while (l1 <= mid)
        b[i++] = a[l1++];

    while (l2 <= high)
        b[i++] = a[l2++];

    for (i = low; i <= high; i++)
        a[i] = b[i];
}

void sort(int low, int high)
{
    int mid;

    if (low < high)
    {
        mid = (low + high) / 2;
        sort(low, mid);
        sort(mid + 1, high);
        merging(low, mid, high);
    }
    else
    {
        return;
    }
}

int main()
{
    int i;
    int arr[max] = {0}, temp, cases, i = 0;
    printf("Enter how many numbers you want to enter : ");
    scanf("%d", &cases);
    temp = cases;
    while (cases--)
        scanf("%d", &arr[i++]);
    cases = temp;

    printf("List before sorting\n");

    for (i = 0; i <= max; i++)
        printf("%d ", a[i]);

    sort(0, cases);

    printf("\nList after sorting\n");

    for (i = 0; i <= max; i++)
        printf("%d ", a[i]);
}