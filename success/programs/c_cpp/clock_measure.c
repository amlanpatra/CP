#include <time.h>
#include<stdio.h>
int main(void) {
	clock_t start, end;
	double cpu_time_used;

	start = clock();
	printf("hello world!\n");
	end = clock();
	cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	printf("%lf\n", cpu_time_used );
}