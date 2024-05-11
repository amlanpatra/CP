#include<stdio.h>

int main(void) {
	int a[] = {2000, 500, 200, 100, 50, 20, 10, 5, 2, 1}, b[10] = {0}, i = 0, num = 0;

	int value = 2020;

	while (i < 11) {
		while (value >= a[i]) {
			value -= a[i];
			num++;
		}
		b[i] = num;
		num = 0;
		++i;
	}

	for (i = 0; i < 10; ++i) {
		if (b[i] != 0)
			printf("%d denominations are : %d\n", a[i], b[i]);
	}
}