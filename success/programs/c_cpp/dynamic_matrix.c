#include <stdio.h>
#include <stdlib.h>
typedef struct
{
    int a[10][10];
} matrix;

void run()
{
#ifndef RUN
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

matrix *p;
matrix get(matrix *);
matrix show(matrix *);
matrix add(matrix *);

int i, j, r, c, size, count;

int main()
{

    run();
    printf("\t\tPROGRAM TO SHOW DIAGONAL SUM AND ADDITION OF 2 MATRICES\n");
    printf("\t\t********************************************************\n");

    printf("How many matrices you want to enter : ");
    scanf("%d", &size);
    p = (matrix *)(malloc((size + 1) * sizeof(matrix)));
    printf("Enter number of rows and cols you want to use : ");
    scanf("%d %d", &r, &c);

    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            (p[size]).a[i][j] = 0;
        }
    }

    for (count = 0; count < size; count++)
    {
        get(&p[count]);
        show(&p[count]);
    }

    printf("\n\n\n\t\t •• MATRIX ADDITION ••\n");
    show(&p[size]);

    return 0;
}

matrix get(matrix *x)
{
    (*x).a[9][9] = 0;

    printf("\n\nEnter values of matrix %d : ", (count + 1));
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            fflush(stdin);
            scanf("%d", &((*x).a[i][j]));
            (p[size]).a[i][j] += (*x).a[i][j];
            if (i == j)
            {
                (*x).a[9][9] += (*x).a[i][j];
                (p[size]).a[9][9] += (*x).a[i][j];
            }
        }
    }
   // return;
}

matrix show(matrix *x)
{
    printf("\n The matrix is : \n");
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            printf("%4d", (*x).a[i][j]);
        }
        printf("\n");
    }
    printf("\n Sum of Diangonals are : %d \n", (*x).a[9][9]);
    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
 //   return;
}