#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void run()
{
#ifndef RUN
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

int main()
{

    vector<int> a1 = {12, 11, 10, 123};
    cout << a1.size() << endl;
    //vector<int>::iterator it = a1.begin();

  

    for (int x : a1)
    {
        cout << x << " ";
    }
}