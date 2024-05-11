#include<stdio.h>
#include<stdlib.h>
struct Node {
	Node *link;
	int data;
} *start, *temp, *temp1;
void get(int limit) {
	start = (Node*)malloc(sizeof(Node));
	temp = start;
	for (int i = 0; i < limit; ++i) {
		scanf("%d", &(temp->data)) ;
		temp->link = (Node*)malloc(sizeof(Node)) ;
		temp = temp->link;
		temp->link = NULL;
	}
}
void show() {
	temp = start;
	while (temp->link != NULL)
	{
		printf("%d", temp->data);
		temp = temp->link;
	}
}
void insert(int index, int value) {
	int count = 1;
	temp = start;
	while (count < (index - 1))
	{
		temp = temp->link;
		count++;
	}
	temp1 = temp->link;
	temp->link = (Node*)malloc(sizeof(Node));
	temp = temp->link;
	temp->data = value;
	temp->link = temp1;

}
void del(int position) {
	int count = 1;
	temp = start;
	while (count < (position - 1))
	{
		temp = temp->link;
		count++;
	}
	temp1 = (*(temp->link)).link;
	temp->link = temp1;
}

int main(void) {
	get(6);
	insert(4, 123);
	show();
	printf("\n");
	del(5);
	show();
}



/*    SAMPLE INPUT


23
12
45
85
12
43

23
12
45
123
85
12
43

23
12
45
123
12
43




14
15
563
7878
4564
4
64
575
63
55
7
86
4
3
66
75
8
567
4345
3343
55
676
774
453
535
3536
6576
977
8978
567
43
12345
*/