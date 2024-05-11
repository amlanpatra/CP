#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	vector<int> v = {12, 324, 453, 242, 56, 57, 884, 43};

	sort(v.begin(), v.end());

	for (int i : v)
	{
		cout << i << ' ';
	}
	return 0;
}