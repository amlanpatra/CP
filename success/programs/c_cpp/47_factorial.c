//factorial
#include <stdio.h>
int main()
{
	double b,i;

	printf("Enter a positive integer : \n");
    scanf("%lf",&b);
    i=b;
    while (b>1)
    {
    	b--;
    	i = b*i;
    }
printf("The factorial is : %lf ",i);
return 0;
}