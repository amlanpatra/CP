#include <iostream>
#include<array>
#include<algorithm>
#define length 4
using namespace std;
int check(array<int, length>, int b);
int32_t main(void) {
	clock_t start, end;
	start = clock();


	array<int, length>a = {1313, 13, 26, 39};


	sort(a.begin(), a.end());
	int gcd = 1, p = 2;

	for (int i = 0; i <= a[0]; ++i)
	{
		while (check(a, p)) {
			for (int i = 0; i < a.size(); ++i)
				a[i] /= p;
			gcd *= p;
		} p++;
	}
	cout << "GCD is : " << gcd;
	end = clock();
	printf("\nTime : %lf", (((double)end - start) / CLOCKS_PER_SEC));
}
int check(array<int, length>a, int b) {
	int p = 0;
	for (int i = 0; i < a.size(); ++i)
		p += a[i] % b == 0 ? 1 : 0;
	return (p == a.size() ? 1 : 0);
}