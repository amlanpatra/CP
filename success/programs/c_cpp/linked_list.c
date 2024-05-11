#include <stdio.h>
#include<stdlib.h>
struct node
{
	int info;
	struct node *next;
} *head, *temp;

int main(void)
{
	freopen("input.txt", "r", stdin);
	head = (struct node*)malloc(sizeof(struct node));
	temp = head;
	for (int i = 0; i < 4; ++i)
	{
		scanf("%d", &(*temp).info);
		printf("%d\n", (*temp).info );
		(*temp).next = (struct node*)malloc(sizeof(struct node));
		temp = (*temp).next;
		(*temp).next = NULL;
	}
}