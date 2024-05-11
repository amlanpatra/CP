#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	freopen("input.txt", "r", stdin);
	char arr[10];
	int sum = 0, sum1 = 0;
	printf("Enter the DOB in dd/mm/yyyy format : \n");
	for (int i = 0; i < 10; ++i)
	{
		scanf("%c", &arr[i]);
		if (arr[i] != '/')
		{
			sum += atoi(&arr[i]);
		}
	}
	printf("entered date is : ");
	for (int i = 0; i < 10; ++i)
	{
		printf("%c", arr[i] );
	}
	while (sum != 0)
	{
		sum1 += (sum % 10);
		sum /= 10;
	}
	sum = (sum1 > 9) ? ((sum1 % 10) + (sum1 / 10) % 10) : sum1;
	printf("\nLucky number is : %d\n", sum);
}