#include <iostream>
using namespace std;

int main()
{
    int t, last_digit;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        if (n < 10)
        {
        }
        else
        {
            last_digit = n % 10;
            while (n > 9)
            {
                n = n / 10;
            }
            int first_digit = n;
            int ans = last_digit + first_digit;
            cout << ans << endl;
        }
    }

    return 0;
}
