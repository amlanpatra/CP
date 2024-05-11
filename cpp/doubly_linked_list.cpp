#include <iostream>
#define max 6
using namespace std;

struct node
{
	int data;
	struct node *next;
	struct node *previous;
};

// Get the value, show , insert, delete, reverse
void get(node *head)
{
	int num;
	head = new node;
	node *temp = head;
	cout << "enter how many numbers : ";
	cin >> num;
	for (int i = 0; i < num; i++)
	{
	}
}

int main(void)
{
	freopen("input.txt", "r", stdin);
	node *head;
	get(head);
}