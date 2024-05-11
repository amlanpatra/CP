#include<iostream>
#include<bitset>
using namespace std;
int main(void)
{
	signed int a = 1, b = 255;


	cout << "Binary of " << a << " is :   " << (bitset<16>)a << endl;
	cout << "Binary of " << b << " is : " << (bitset<16>)b << endl;
	cout << "                 -------------------" << endl;
	cout << "Binary          : " << (bitset<16>)(a + b) << endl ;

	cout << "Decimal         : " << a + b << endl;
}