#include <iostream>
using namespace std;
int zeros(int);
int zeros(int num)
{
    int count = 0;
    for (int i = 5; num / i > 0; i *= 5)
        count += num / i;
    return count;
}

int main(void)
{
    int cases, num;
    cin >> cases;
    while (cases--)
    {
        cin >> num;
        cout << zeros(num) << endl;
    }
}
