#include <stdio.h>
#include<math.h>
int main(void)
{
	int rad;
	float area, circum, pi=3.1416;
	printf("Enter radius : ");
	scanf("%d",&rad);
	//printf("Enter second number: ");
	//scanf("%d",&b);
	/*if (a>=b)
	a=a-b;
	else
	a=b-a;*/
	area = pi*(pow(rad,2));
	circum= 2*pi*rad;

	printf("The radius is %d",rad);
	printf("\nThe area is %f",area);
	printf("\nThe circumference is %f",circum);

}