#include<iostream>
#include<bitset>
using namespace std;
int main(void)
{
	int a = 5, b = 6;
	cout << "a : " << (bitset<3>)a << "  b : " << (bitset<3>)b << endl;
	a ^= b;
	cout << "a is after a^= b : " << (bitset<3>)a << endl;
	b ^= a;
	cout << "b is after b^= a : " << (bitset<3>)b << endl;
	a ^= b;
	cout << "a is after a^= b : " << (bitset<3>)a << endl;
	cout << a << ' ' << b;
}