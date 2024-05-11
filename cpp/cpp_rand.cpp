#include <iostream>
#define MAX 12
using namespace std;

int main(void)
{
    srand(time(0));
    int x = rand();
    x = 100 + x % 100;
    cout << x << endl;

    // x = x % 26;
}

// 65 - 90 .. 97-122
