#include <bits/stdc++.h>
#define p b
using namespace std;

int32_t main(void) {
//freopen("input.txt","r",stdin);
	clock_t start, end;
	start = clock();

	std::vector<int> v{12, 13, 14};

	for (auto i : v)
		cout << i << '\n';

	cout << "count is : " << count(v.begin(), v.end(), 1) << '\n';
	for (auto i : v)
		cout << i << '\n';


	end = clock();
	printf("\nTime :- %lf", (((double)end - start) / CLOCKS_PER_SEC));
}