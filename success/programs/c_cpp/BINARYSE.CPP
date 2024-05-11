#include<stdio.h>
int main(void)
{
	freopen("input.txt", "r", stdin);

	int i, mid, last, first, n, search, a[8];

	printf("\nenter the no of elements");
	scanf("%d", &n);

	printf("\nenter the array elements");
	for (i = 0; i < n; i++)
		scanf("%d", &a[i]);


	printf("\nenter the element to be searched");
	scanf("%d", &search);

	first = 0;
	last = n - 1;
	mid = (first + last) / 2;
	while (first <= last)
	{
		if (a[mid] < search)
			first = mid + 1;
		else if (a[mid] == search)
		{
			printf("\n %d element present at index %d", search, mid + 1);
			break;
		}
		else
			last = mid - 1;

		mid = (first + last) / 2;
	}
}