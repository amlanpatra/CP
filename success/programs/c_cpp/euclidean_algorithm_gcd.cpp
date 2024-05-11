#include<bits/stdc++.h>
using namespace std;
int32_t main(void) {
	clock_t start, end;
	start = clock();

	int a = 3768, b = 1701, x = a, y = b;

	while (a % b > 0) {
		int temp = a % b;
		a = b;
		b = temp;
	}


	cout << b << " is the GCD of " << x << " and " << y;

	end = clock();
	printf("\nTime : %lf", (((double)end - start) / CLOCKS_PER_SEC));

}


//  a     b
// 126 = 12 * 10 + 6
// 12 = 6 * 2 + 0
// here after one operation , a becomes b and b becomes a%b until a%b becomes 0.