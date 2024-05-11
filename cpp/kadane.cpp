#include <iostream>
using namespace std;
int main(void)
{
    int arr[] = {2, 3, 8, 12, -18, 13};
    int sum = arr[0];
    int max = arr[0];

    for (int i = 1; i < 6; i++)
    {
        sum = sum + arr[i];
        sum = (sum < 0) ? 0 : sum;
        // max = (sum > max) ? sum : max;
        if (sum > max)
        {
            max = sum;
            cout << "position : " << i << " value is " << arr[i] << "    max is " << max << endl;
        }
    }
    cout << max;
}
