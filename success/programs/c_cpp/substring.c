#include<stdio.h>
#include<string.h>

void run()
{
#ifndef RUN
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}


int main()
{
    run();
    char a[25] = "hi there";
    char b[25] = "hello world";
    puts(a);
    puts(b);

    if (strstr(a,b)==NULL)
    {
        printf("Not present");
    }
    else
    {
        printf("Yes present");
    }
    
    return 0;
}