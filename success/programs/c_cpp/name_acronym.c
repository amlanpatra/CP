#include <stdio.h>
#include <string.h>

void run()
{
#ifndef RUN
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

int main()
{
    int i = 0, j, k = 0, x, y;
    run();
    char a[] = "Amlan Patra";
    char b[10];
    y = sizeof(a);
    for (x = 0; x < y; x++)
    {

        j = (int)a[x];
        if (j == 32)
        {
            b[k] = a[x + 1];
            k++;
        }
        else if (x == 0)
        {
            b[k] = a[x];
            k++;
        }
    }
    for (i = 0; i < k; i++)
    {
        printf("%c ", b[i]);
    }

    return 0;
}