#include <bits/stdc++.h>
using namespace std;

int32_t main() {
	int a, b, num;

	for (num = 1; num < 5000; ++num)
	{
		a = num;
		b = 0;
		while (a % 4 == 0) {
			b = (a == 4) ? 1 : 0;
			a /= 4;
			if (b == 1)
				cout << num << ' ';
		}
	}

	return 0 ;
}