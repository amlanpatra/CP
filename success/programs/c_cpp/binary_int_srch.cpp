#include<iostream>
using namespace std;

int main(void)
{
	int a[] = {12, 21, 23, 24, 43, 45, 54, 55, 56, 58, 78, 89, 95, 100, 123, 134, 156, 234};
	int start, end, middle, flag = 0, num = 58;

	start = 0;
	end = (sizeof(a) / sizeof(a[0])) - 1;
	middle = (start + end) / 2;

	while (end - start != 1)
	{
		if (num < a[middle])
		{
			end = middle;
			middle = (start + end) / 2;
		}
		else
		{
			start = middle;
			middle = (start + end) / 2;
		}
	}

	(a[middle] != num) ? (cout << "The number " << num << " is not present.") : (cout << "The number " << num << " is present." << "\na[" << middle << "] is : " << a[middle]);
}