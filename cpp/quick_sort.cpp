#include<iostream>
using namespace std;

int partition(int* arr, int begin, int end) {		// begin is starting index, here is 0; end is ending index

	int i = begin - 1, j;
	for (j = begin; j < end; j++) {
		cout << "i is " << i << '\n';
		cout << "j is " << j << '\n';
		if (arr[j] < arr[end]) {
			cout << "after incrementing a[i] is " << arr[i + 1] << ' ';
			cout << "   a[j] is " << arr[j] << '\n';
			i++;
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;

			cout << "swapped value of a[i] is " << arr[i] << " and a[j] is " << arr[j] << '\n';
			cout << "\n\n";
		}
		else
			cout << "continue\n\n";
	}
	for (int p = 0; p <= end; ++p)
	{
		cout << arr[p] << ' ';
	}
	return ++i;
}




void quicksort(int* arr, int begin, int end) {

	int median = partition(arr, begin, end);
	// for (int i = 0; i < 3; ++i)

	/* code */

	while (begin != end)
	{
		partition(arr, begin, median - 1);
		partition(arr, median, end);
	}
}





int main(void) {
	freopen("input.txt", "r", stdin);
	int a[6] = {0};
	for (int i = 0; i < 6; ++i)
		cin >> a[i];

	quicksort(a, 0, 5);



	cout << "\n\n\n\n\n";

	for (int i = 0; i < 6; ++i)
	{
		cout << a[i] << " ";
	}
}

