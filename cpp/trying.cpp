#include <bits/stdc++.h>
using namespace std;
struct Node {
	int data;
	vector<Node*>children;
};

Node *newNode(int key) {
	Node *temp = new Node;
	temp->data = key;
	return temp;

}

Node *construct(int arr[], int n ) {
	Node *root = NULL;
	stack<Node*>st;
	for (int i = 0; i < n; i++) {
		if (arr[i] == -1) {
			st.pop();
		} else {
			Node *t = newNode(arr[i]);
			if (st.size() > 0) {
				st.top()->children.push_back(t);
			} else {
				root = t;
			}
			st.push(t);
		}
	}
	return root;
}

void traversals(Node *node)
{
	cout << "Node Pre " << node->data;

	for (Node child : node->children) {
		cout << "Edge Pre " << node->data << "--"  << child.data;
		traversals(&child);
		cout << "Edge Post " << node->data  << "--" << child.data;
	}
	cout << "Node Post " << node->data;

}

int main() {
	int n;
	cin >> n;
	int arr[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	Node *root = construct(arr, n);
	traversals(root);
}











