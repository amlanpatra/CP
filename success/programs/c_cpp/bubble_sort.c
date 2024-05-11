//Bubble sort
#include<stdio.h>
int main(void)
{
	int a[100], n, i, temp, start = 0, count = 1;

	printf("How many numbers you want to enter : \n");
	scanf("%d", &n);
	for (i = 0; i < n; ++i)
	{
		scanf("%d", &(a[i]));
	}

	while (start < n)
	{
		while ((start + count) < n)
		{
			if (a[start] > a[start + count])
			{
				//swapping numbers
				temp = a[start];
				a[start] = a[start + count];
				a[start + count] = temp;
			}
			count++;
		}
		start++;
		count = 0;
	}

	for (int i = 0; i < n; ++i)
	{
		printf("%d\n", a[i] );
	}
}