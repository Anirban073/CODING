#include<iostream>
#include<stack>
#include<queue>
#include<limits.h>
using namespace std;

class Node{
public:
    int val;
    Node* left;
    Node* right;

    Node(int val){
        this->val = val;
        this->left = NULL;
        this->right = NULL;
    }
};

Node* constructBT(int arr[], int size){
    if(size == 0) return NULL;
    queue<Node*>q;
    Node* root = new Node(arr[0]);
    q.push(root);
    int i = 1;

    while(q.size() != 0 && i<size){
        Node* temp = q.front();
        q.pop();
        Node* l;
        Node* r;

        if(i < size && arr[i] != INT_MIN) l = new Node(arr[i]);
        else l = NULL;
        i++;

        if(i < size && arr[i] != INT_MIN) r = new Node(arr[i]);
        else r = NULL;
        i++;

        temp->left = l;
        temp->right = r;

        if(l != NULL) q.push(l);
        if(r != NULL) q.push(r);
    }
    return root;
}

void displayByStack(Node* root){
    stack<Node*> s;
    s.push(root);
    while(s.size()){
        Node* temp = s.top();
        s.pop();
        cout << temp->val << "  ";
        if(temp->right != NULL) s.push(temp->right);
        if(temp->left != NULL) s.push(temp->left);
    }
    cout << endl;
}

int main(){
    int arr[] = {1, 2, 3, 4, 5, INT_MIN, 6, INT_MIN, INT_MIN, 7, 8, 9, INT_MIN};
    int size = sizeof(arr) / sizeof(arr[0]);

    Node* root = constructBT(arr, size);

    displayByStack(root);
    cout << endl;


    return 0;
}