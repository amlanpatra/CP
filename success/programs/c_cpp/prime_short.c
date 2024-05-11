#include<stdio.h>
#include<math.h>
int main(void)
{
	int a = 10378;
	(((a - 1) % 6 == 0) || ((a + 1) % 6 == 0)) ? (printf("Prime number\n")) : (printf("Non Prime number\n"));
}


