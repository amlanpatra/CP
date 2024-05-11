#include<stdio.h>
#include<time.h>
int gcd(int, int);
int main()
{
  clock_t start, end;
  start = clock();


  int a[4] = {12, 16, 18, 24};
  int i, b, final;
  b = sizeof(a) / sizeof(a[0]);

  final = gcd(a[0], a[1]);

  for (i = 2; i < b; i++)
    final = gcd(final, a[i]);
  printf("GCD : %d \n", final);




  end = clock();
  printf("Time : %lf", (((double)end - start ) / CLOCKS_PER_SEC));
  return 0;
}

int gcd(int a, int b) {
  if (a < b) {
    a ^= b;
    b ^= a;
    a ^= b;
  }

  while (a % b > 1) {
    int temp = a % b;
    a = b;
    b = temp;
  }
  return (a % b == 1) ? 1 : b;
}