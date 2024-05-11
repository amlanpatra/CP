#include <iostream>
using namespace std;
void run()
{
#ifndef RUN
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}


int main(void)
{
    run();
    int r, c, i, j, a[5][5],b[25],x=0;
    scanf("%d %d",&r,&c);

    printf("The initial matrix is : \n\n");

    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            scanf("%d", &a[i][j]);
            b[x]=a[i][j];   
            x++;
        }
    }

    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            printf(" %d", a[i][j]);
        }
        printf("\n");
    }

    printf("\n\nThe final matrix is : \n\n");

    for (i = 0; i < c; i++)
    {
        for (j = 0; j < r; j++)
        {
            printf(" %d", a[j][i]);
        }
        printf("\n");
    }

 //   return 0;
}