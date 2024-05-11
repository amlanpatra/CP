#include<stdio.h>
int pallindrome(int);
int main(void)
{
	int a = 25897, num = a, low, high;

	while (pallindrome(a))
	{
		a--;
	}
	low = a;
	a = num;
	while (pallindrome(a))
	{
		a++;
	}
	high = a;
	a = num;
	a = ((a - low) < (high - a)) ? low : high;
	printf("Nearest Pallindrome of %d is : %d\n", num, a);
}


int pallindrome(int a) {
	int sum = 0, num = a;
	while (a > 0) {
		sum = sum * 10 + a % 10;
		a /= 10;
	}
	(sum == num) ? (num = 0) : (num = 1);
	return num;
}