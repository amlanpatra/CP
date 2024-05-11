#include <stdio.h>
int main(void)
{
	int a, b;
	printf("Enter fist number : ");
	scanf("%d",&a);
	printf("Enter second number: ");
	scanf("%d",&b);
	if (a>=b)
	a=a/b;
	else
	a=b/a;
	printf("The division is %d",a);
}