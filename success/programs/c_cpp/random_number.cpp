#include <iostream>
#include <stdlib.h>
#include<algorithm>
using namespace std;

int main(void) {
	int a[100] = {0};
	clock_t start, end;
	double all_time;
	start = clock();


	for (int i = 0; i < 100; ++i)
		a[i] = ((rand() % 100) + 1);


	sort(a, a + 100);

	for (int i = 0; i < 100; ++i)
		cout << a[i] << ' ';

	end = clock();
	all_time = ((double)(end - start )) / CLOCKS_PER_SEC;
	printf("\n%lf\n", all_time);
}