// traingle pattern 2
#include <stdio.h>
int main()
{
	int a,b;
	for (a=11;a>=1;a--)
	{
		for (b=a;b>=1;b--)
		{
			printf("*");
		}
		printf("\n");
	}
}