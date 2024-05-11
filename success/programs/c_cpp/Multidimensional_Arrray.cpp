#include <iostream>
using namespace std;
int main()
{
   int array1[2][3] = {{13,10,12},{14,15,26}};
   for (int y=0;y<2;)
   {
       for (int x=0;x<3;)
       {
           cout<<" "<<array1[y][x];
           x+=1;
       }
       cout<<"\n";
       y+=1;
       
   }

    return 0;
}
