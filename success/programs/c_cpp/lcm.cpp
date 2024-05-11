#include<stdc++.h>
using namespace std;

int lcm(vector<int>);
//int check23(vector<int>);
int main(void)
{	freopen("input.txt", "r", stdin);

	int incoming;
	vector<int> a1;
	for (int i = 0; i < 13; i++)
	{
		cin >> incoming;
		a1.push_back(incoming);
	}

	cout << lcm(a1);

}



int lcm(vector<int> x)
{
	sort(x.begin(), x.end());
	long limit;

	int j = 1, count = 0;
	bool check = true;
	while (check)
	{
		limit = (x.back() * j);
		j++;
		count = 0;

		for (int z : x)
		{
			if (limit % z == 0)
			{
				count++;
			}
		}
		if (count == x.size())
		{
			check = false;
		}
	}
	return limit;
}