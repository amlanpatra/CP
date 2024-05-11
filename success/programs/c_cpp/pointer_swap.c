#include <stdio.h>

void run()
{
#ifndef RUN
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

void swap(int *, int *);



int main()
{
    run();
    int a = 250;
    int b = 300;
    swap(&a, &b);
    return 0;
}
void swap(int *x, int *y)
{
    /*  int z= *x;
    *x = *y;
    *y = z;*/

    *x = *x + *y;
    *y = *x - *y;
    *x = *x - *y;
    printf("%d %d", *x, *y);
}