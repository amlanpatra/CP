// Entered number is positive or negaitve
#include<stdio.h>
int main()
{
	int a;
	printf("Enter a number : \n");
	scanf ("%d",&a);
	if (a>0)
	{
		printf("%d is a positive number.\n",a );
	}
	else if (a==0)
	{
		printf("%d is neither negative nor positive.It is zero.\n",a );
	}
	else
	{
		printf("%d is a negative number.\n",a );
	}
return 0;
}