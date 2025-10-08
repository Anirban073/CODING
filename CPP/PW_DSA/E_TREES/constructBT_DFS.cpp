#include<iostream>
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
        left = NULL;
        right = NULL;
    }
};

Node* construct(int arr[], int size){
    if (size == 0) return NULL;
    queue<Node*>q;
    Node* root = new Node(arr[0]);
    q.push(root);

    int i=1;
    int j=2;
    while(q.size() > 0 && i < size){
        Node* temp = q.front();
        q.pop();
        Node* l;
        Node* r;
        if(arr[i] != INT_MIN){
            l = new Node(arr[i]);
        }
        else{
            l = NULL;
        }
        if(j < size && arr[j] != INT_MIN){
            r = new Node(arr[j]);
        }
        else{
            r = NULL;
        }

        if(l != NULL) q.push(l);
        if(r != NULL)q.push(r);

        temp->left = l;
        temp->right = r;

        i += 2;
        j += 2;
    }
    return root;
}

void NthDisplay(Node* root){
    queue<Node*>q;
    q.push(root);

    while(q.size() > 0){
        Node* temp = q.front();
        q.pop();
        cout << temp->val << "  ";
        if(temp->left != NULL) q.push(temp->left);
        if(temp->right != NULL) q.push(temp->right);
    }
}


int main(){
    int arr[] = {1,2,3,4,5,INT_MIN, 6, INT_MIN, INT_MIN, 7, 8, 9};
    int size = sizeof(arr) / sizeof(arr[0]);

    Node* root = construct(arr, size);

    NthDisplay(root);

    return 0;
}

// #include<iostream>
// #include<queue>
// #include<limits.h>
// using namespace std;

// class Node{
// public:
//     int val;
//     Node* left;
//     Node* right;

//     Node(int val){
//         this->val = val;
//         this->left = NULL;
//         this->right = NULL;
//     }
// };

// Node* constructBT(int arr[], int size){
//     queue<Node*>q;
//     Node* root = new Node(arr[0]);
//     q.push(root);
//     int i = 1;
//     int j = 2;
//     while(q.size() > 0 && i < size){
//         Node* temp = q.front();
//         q.pop();

//         Node* leftNode;
//         Node* rightNode;

//         if(arr[i] == INT_MIN){
//             leftNode = NULL;
//         }
//         else{
//             leftNode = new Node(arr[i]);
//         }
//         if (j >= size || arr[j] == INT_MIN) {
//             rightNode = NULL;
//         }
//         else {
//             rightNode = new Node(arr[j]);
//         }

//         if(leftNode != NULL){
//             q.push(leftNode);
//         }
//         if(rightNode != NULL){
//             q.push(rightNode);
//         }

//         temp->left = leftNode;
//         temp->right = rightNode;

//         i += 2;
//         j += 2;
//     }
//     return root;
// }

// int level(Node* root){
//     if(root ==  NULL) return 0;
//     return 1 + max(level(root->left), level(root->right));
// }

// void nthSearch(Node* root, int cur, int level){
//     if(root == NULL) return;
//     if(cur == level){
//         cout << root->val << "  ";
//         return;
//     }
//     nthSearch(root->left, cur+1, level);
//     nthSearch(root->right, cur+1, level);
// }

// void levelOrder(Node* root){
//     int lev = level(root);
//     for(int i=1; i<=lev; i++){
//         nthSearch(root, 1, i);
//         cout << endl;
//     }
// }

// int main(){
//     int arr[12] = {1, 2, 3, 4, 5, INT_MIN, 6, INT_MIN, INT_MIN, 7, 8, 9};

//     Node* root = constructBT(arr, 12);

//     levelOrder(root);

//     return 0;
// }

