#include<iostream>
#include<limits.h>
#include<queue>
using namespace std;
class Node{
public:
    int val;
    Node* left;
    Node* right;
    Node(int val){
        this->val = val;
        left = NULL;
        right = NULL;
    }
};
Node* create(int arr[], int size){
    if(size == 0) return NULL;
    queue<Node*>q;
    Node* root = new Node(arr[0]);
    q.push(root);

    int i=1;
    while(!q.empty() && i<size){
        Node* temp = q.front();
        q.pop();
        Node* l;
        Node* r;
        if(i<size && arr[i] != INT_MIN){
            l = new Node(arr[i]);
        }
        else{
            l = NULL;
        }
        i++;
        if(i<size && arr[i] != INT_MIN){
            r = new Node(arr[i]);
        }
        else{
            r = NULL;
        }
        i++;

        temp->left = l;
        temp->right = r;

        if(l != NULL) q.push(l);
        if(r != NULL) q.push(r);
    }
    return root;
}

int mul(Node* root){
    if(root == NULL) return 1;
    return root->val * mul(root->left) * mul(root->right);
}
int main(){
    int arr[7] = {1,2,3,4,5,INT_MIN,6};
    Node* root = create(arr, 7);
    cout << " multiplication value : " << mul(root);
    return 0;
}