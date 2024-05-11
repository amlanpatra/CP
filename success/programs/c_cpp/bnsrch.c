#include<stdio.h>
int main(void)
{
	int a[100], start, end, middle, flag = 0, num, limit;

	freopen("input.txt", "r", stdin);

	printf("Enter the limit : ");
	scanf("%d", &limit);

	printf("\nEnter the numbers : ");

	for (int i = 0; i < limit; ++i)
		scanf("%d", &a[i]);

	printf("\nEnter the number you want to search : ");
	scanf("%d", &num);

	start = 0;
	end = limit;
	middle = (start + end) / 2;
	while (end - start != 1)
	{
		if (num < a[middle])
			end = middle;
		else
			start = middle;
		middle = (start + end) / 2;
	}
	(a[middle] != num) ? printf("\n%d is NOT Present", num ) : printf("\n%d is Present", num );
}