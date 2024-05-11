#include <iostream>
using namespace std;
int zeros(int);
int zeros_at_end(long long);

int main(void)
{
	int i = 100;
	cout << "the trailing 0 is : " << zeros(i) << endl;
	cout << "zeros at end : " << zeros_at_end(i) << endl;
}

int fact_rev(long long fact)
{
	int zero = zeros_at_end(fact);
	return zero;
}

int zeros(int num)
{
	int count = 0;
	for (int i = 5; num / i > 0; i *= 5)
	{
		count += num / i;
	}
	return count;
}

int zeros_at_end(long long num)
{
	int count = 0;
	while (num % 10 == 0)
	{
		count++;
		num /= 10;
	}
	return count;
}
