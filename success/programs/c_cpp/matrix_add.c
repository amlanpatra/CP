#include <stdio.h>

void run()
{
#ifndef RUN
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

typedef struct
{
    int a[10][10];

} matrix;
matrix m1, m2, m3;

int r, c, i, j;

matrix get();
void show(matrix);
matrix add(matrix, matrix);

int main()
{
    run();
    printf("PROGRAM TO SHOW DIAGONAL SUM AND ADDITION OF 2 MATRICES\n");
    printf("********************************************************\n");
    printf("\nEnter how many rows and columns you want to use : ");
    scanf("%d*%d", &r, &c);

    m1 = get();
    show(m1);

    m2 = get();
    show(m2);

    m3 = add(m1, m2);

    printf("\n Diagonal sum of 1st matrix : %d", m1.a[9][9]);
    printf("\n Diagonal sum of 2nd matrix : %d \n", m2.a[9][9]);

    printf("\n\n\n •• MATRIX ADDITION ••\n");
    show(m3);
    return 0;
}

matrix get()
{
    matrix x;
    x.a[9][9] = 0;
    printf("\n\nEnter values of matrix : ");
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            fflush(stdin);
            scanf("%d", &x.a[i][j]);
            if (i == j)
                x.a[9][9] += x.a[i][j];
        }
    }
    return (x);
}

void show(matrix x)
{
    printf("\n The matrix is : \n");
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            printf("%4d", x.a[i][j]);
        }
        printf("\n");
    }
    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
}

matrix add(matrix x, matrix y)
{
    matrix z;

    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            z.a[i][j] = x.a[i][j] + y.a[i][j];
        }
    }
    return z;
}