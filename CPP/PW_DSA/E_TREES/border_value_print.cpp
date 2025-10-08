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
    while(q.size() && i < size){
        Node* temp = q.front();
        q.pop();
        Node* l;
        Node* r;
        if (i < size && arr[i] != INT_MIN) l = new Node(arr[i]);
        else l = NULL;
        i++;
        if(i < size && arr[i] !=INT_MIN) r = new Node(arr[i]);
        else r = NULL;
        i++;
        if(l != NULL) q.push(l);
        if(r != NULL) q.push(r);
        temp->left = l;
        temp->right = r;
    }
    return root;
}

void leftPrint(Node* root){
    if(root == NULL) return;
    if(root->left == NULL && root->right == NULL) return;
    cout << root->val << "  ";
    leftPrint(root->left);
    if(root->left == NULL) leftPrint(root->right);
}

void leafPrint(Node* root){
    if(root == NULL) return;
    if(root->left == NULL && root->right == NULL){
        cout << root->val << "  ";
    }
    leafPrint(root->left);
    leafPrint(root->right);
}

void rightPrint(Node* root){
    if(root == NULL) return;
    if(root->left == NULL && root->right == NULL) return;
    if(root->right == NULL) rightPrint(root->left);
    rightPrint(root->right);
    cout << root->val << "  ";
}

void display(Node* root){
    if(root == NULL) return;
    queue<Node*>q;
    q.push(root);
    while(!q.empty()){
        Node* temp = q.front();
        q.pop();
        cout << temp->val << "  ";
        if(temp->left != NULL) q.push(temp->left);
        if(temp->right != NULL) q.push(temp->right);
    }
}

void borderPrint(Node* root){
    leftPrint(root);
    leafPrint(root);
    rightPrint(root->right);
}

int main(){
    int arr[] = {1,2,3,4,5,INT_MIN,6,7,INT_MIN,8,INT_MIN,9,10,INT_MIN,11,INT_MIN,12,INT_MIN,13,INT_MIN,14,15,16,INT_MIN,17,INT_MIN,INT_MIN,18,INT_MIN,19,INT_MIN,INT_MIN,INT_MIN,20,21,22,23,INT_MIN,24,25,26,27,INT_MIN,INT_MIN,28,INT_MIN,INT_MIN};

    int size = sizeof(arr)/sizeof(arr[0]);

    Node* root = constructBT(arr, size);
    // display(root);
    borderPrint(root);


    return 0;
}