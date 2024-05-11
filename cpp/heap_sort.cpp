#include <iostream>
#define max 6
using namespace std;
struct node
{
	int data;
	struct node *child1;
	struct node *child2;
	struct node *parent;
};

void heapify(int *arr, int size)
{
	node head;
	head.data = arr[0];
	head.next = new node;
}

int main()
{
	freopen("input.txt", "r", stdin);
	int a[max];
	for (int i = 0; i < max; ++i)
		cin >> a[i];
	heapify(a, max);
}