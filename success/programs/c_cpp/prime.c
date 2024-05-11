#include<stdio.h>
int main()
{
	int a = 293;
	int i = 2;
	while (i < a / i)
	{
		if (a % i == 0) {
			printf("%d is not a prime number. Its smallest factor is %d \n", a, i );
			return 0;
		}
		i++;
	}
	printf("%d is a Prime number\n", a );
	return 0;
}