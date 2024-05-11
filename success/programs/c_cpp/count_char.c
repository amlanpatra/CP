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
    int i=0,j,k=0,x,y;
    run();
    char a[] = "hi there. I am learning C";
    y = sizeof(a);
    for ( x = 0; x < y; x++)
    {
        
    
        j=(int)a[x];
        if ((j==73) || (j==105))
        {
            k++;
        }
       
    }
    printf("Here I is %d number of times", k);

    return 0;
}