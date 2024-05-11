// SINGLY LINKED LIST BY ME
#include<iostream>
using namespace std;
struct Node
{
	Node *link;
	int data;
} *start, *temp, *temp1;


class list
{
public:
	void get(int limit)
	{
		start = new Node;
		temp = start;
		for (int i = 0; i < limit; ++i)
		{
			cin >> temp->data ;
			//temp->data = i;
			temp->link = new Node ;
			temp = temp->link;
			temp->link = NULL;
		}
	}


	void show()
	{
		temp = start;
		while (temp->link != NULL)
		{
			cout << temp->data << endl;
			temp = temp->link;
		}
	}

	void insert(int index, int value)
	{
		int count = 1;
		temp = start;
		while (count < (index - 1))
		{
			temp = temp->link;
			count++;
		}
		temp1 = temp->link;
		temp->link = new Node;
		temp = temp->link;
		temp->data = value;
		temp->link = temp1;

	}


	void del(int position)
	{
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

};


int main()
{

	freopen("input.txt", "r", stdin);
	//freopen("input.txt", "w", stdout);

	list l1;
	// get funcion input is number of elements
	l1.get(12);
	//change function inputs are position(not index) of change and the value
	l1.insert(4, 123);
	// show function shows all the elements currently
	l1.show();
	cout << endl;
	// del function deletes the element at the given positon
	l1.del(4);
	l1.show();

	return 0;
}



/*    SAMPLE INPUT

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