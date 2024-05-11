#include <stdio.h>
int main(void)
{
    int n, i;
    printf("Enter a number : ");
    scanf("%d", &n);
    for (i = 2; i <= n / 2; i++)
    {
        if (n % i == 0)
        {
            break;
        }
    }
    if (i > n / 2)
    {
        printf("%d is a prime number .", n);
    }
    else
    {
        printf("%d is not a prime number . ", n);
    }
}
