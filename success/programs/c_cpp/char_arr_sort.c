#include<stdio.h>
#define max 5
char* sorting(char*);

int main(void) {

	char arr[max] = {'A', 'm', 'l', 'a', 'n'};
	char* a = sorting(arr);

	for (int i = 0; i < max; ++i)
	{
		printf("%c\n", *a );
		a++;
	}
}



// Using Bubble sort
char* sorting(char a[max])
{

	int b = max;
	int d = 0;
	int temp, j, start = 0, count = 1;

	while (start < b)
	{
		while ((start + count) < b)
		{
			if (a[start] > a[start + count])
			{
				//swapping numbers
				temp = (int)a[start];
				a[start] = a[start + count];
				a[start + count] = (char)temp;
			}
			count++;
		}
		start++;
		count = 0;
	}
	return a;
}


