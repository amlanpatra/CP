#include<bits/stdc++.h>
using namespace std;



class tree
{
public:
	struct node
	{
		int value;
		struct node* left_node;
		struct node* right_node;
		int height;
	};

	node* head = new node, *temp = head;
	tree(int a) {
		head->value = a;
	}


	void insert(int a) {
		if (a < temp->value) {
			temp -> left_node = new node;
			(temp->left_node) ->value = a;
		}
		else if (a > temp-> value) {
			temp-> right_node = new node;
			(temp -> right_node)-> value = a;
		}
	}















};


int main(void) {
#define root head->value
	tree a(23);
	cout << a.root;


}