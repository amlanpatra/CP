#include<stdio.h>

int main(void) {
	int a[] = {8, 6, 5, 3, 1, 2, 2, 1};
	int b[10] = {0};
	int sum = 0, j = 0, k = 0, l = 0;

	for (int i = 0; i < sizeof(a) / sizeof(a[0]); ++i)
	{
		if (a[i] % 3 == 0) {
			(sum += a[i]);
		}

		else if (a[i] == 1) {
			k++;
		}

		else if (a[i] == 2) {
			l++;
		}

		else {
			b[j] = a[i];
			j++;
		}
	}

	for (int i = 0; i <= j; ++i) {
		if ((l != 0) && ((b[i] + 2) % 3 == 0))
		{
			sum += b[i] + 2;
			l--;
		}
		else if ((k != 0) && ((b[i] + 1) % 3 == 0))
		{
			sum += b[i] + 1;
			k--;
		}
	}
	printf("Maximum sum is : %d\n", sum );
}