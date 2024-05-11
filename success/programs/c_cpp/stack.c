// Stack program to Show Functions push, pop, top, display
// Only for Integer values
// Change value of max to increase stack capacity
#include<stdio.h>
#define max 10
int a = 1, b = 0, top = 0;
int stack[max];
int *p = &b;

int main(void)
{
	int x;
	//freopen("input.txt", "r", stdin);
	while (a)
	{
		{
			printf("\n\nWhat operation you want to perform : Push(1), Pop(2), Top(3), Display_Stack(4) or Exit(5) ? \n Press any 1/2/3/4/5 for the operations : ");
			scanf("%d", &x);
			switch (x)
			{
			case 1:
				printf("\n\nEnter value to Push : \n");
				scanf("%d", &b);
				(top < max) ? (stack[top] = *p) : printf("\nStack is filled. Please pop to push value.\n");
				top++;
				break;

			case 2:
				printf("\n\nStack Popped.\n");
				top--;
				break;

			case 3:
				if (top > 0)
					printf("\n\nTop value is : %d\n", stack[top - 1] );
				else
					printf("\n\nStack is empty\n");
				break;

			case 4:
				if (top > 0) {
					printf("\n\nThe entire stack : \n");
					for (int i = top - 1; i >= 0; --i)
						printf("%d\n", stack[i] );
				}
				else
					printf("\n\nStack is empty\n");
				break;

			case 5:
				a = 0;
				break;

			default:
				printf("\n\nPlease enter Correct option...\n\n");
			}
		}

	}
}