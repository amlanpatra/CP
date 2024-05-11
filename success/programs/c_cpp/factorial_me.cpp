#include <iostream>
using namespace std;
#define max 60000 //size of the array containing the value

int main(void)
{
	//freopen("input.txt", "r", stdin);
	int num = 15000; // = 15000; //factorial to be calculated
	//printf("Enter the number : ");
	//scanf("%d", &num);

	long arr[max] = {0};
	int count = 0;
	int num_copy = num;
	int carry = 0;

	while (num != 0)
	{
		num = (int)(num / 10);
		count++;
	}

	num = num_copy ;

	int arr_start = max - (count + 1);
	int arr_end = max - 1;

	for (int i = (max - 1); i > arr_start ; i--)
	{
		arr[i] = num % 10;
		num = (int)(num / 10);
	}


	num = num_copy;
	num--;

	while (num != 1)
	{
		for (int i = arr_end ; i > arr_start ; --i)
		{

			arr[i] = arr[i] * num;
			arr[i] += carry;
			carry = (int)(arr[i] / 10);
			arr[i] = arr[i] % 10;

			if ((i == (arr_start + 1)) && (carry != 0))
			{
				arr_start--;
			}
		} num--;
	}

	cout << " arr_start : " << arr_start << "   arr_end : " << arr_end << "\n";

	for (int i = arr_start + 1; i < max; ++i)
	{
		cout << ' ' << arr[i];
	}
	cout << "\ncarry : " << carry;

	int zeros = 0;

	int i = arr_end;

	while (arr[i] == 0)
	{
		i--;
		zeros++;
	}

	cout << "\nZeros at end : " << zeros ;
}