// #include<iostream>
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

// void nthSearch(Node* root, int cur, int level){
//     if(root == NULL) return;
//     if(cur == level){
//         cout << root->val << "  ";
//     }
//     nthSearch(root->left, cur+1, level);
//     nthSearch(root->right, cur+1, level);
// }

// int main(){
//     Node* a = new Node(1);
//     Node* b = new Node(2);
//     Node* c = new Node(3);
//     Node* d = new Node(4);
//     Node* e = new Node(5);
//     Node* f = new Node(6);
//     Node* g = new Node(7);
//     a->left = b;
//     a->right = c;
//     b->left = d;
//     b->right = e;
//     c->left = f;
//     c->right = g;


//     nthSearch(a,1,1);
//     cout << endl;
//     nthSearch(a,1,2);
//     cout << endl;
//     nthSearch(a,1,3);
//     cout << endl;
//     nthSearch(a,1,4);
//     cout << endl;

//     return 0;
// }





#include<iostream>
#include<algorithm>
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

int level(Node* root){
    if(root ==  NULL) return 0;
    return 1 + max(level(root->left), level(root->right));
}

void nthSearch(Node* root, int cur, int level){
    if(root == NULL) return;
    if(cur == level){
        cout << root->val << "  ";
        return;
    }
    nthSearch(root->right, cur+1, level);
    nthSearch(root->left, cur+1, level);
}

void levelOrder(Node* root){
    int lev = level(root);
    for(int i=1; i<=lev; i++){
        nthSearch(root, 1, i);
        cout << endl;
    }
}

int main(){
    Node* a = new Node(1);
    Node* b = new Node(2);
    Node* c = new Node(3);
    Node* d = new Node(4);
    Node* e = new Node(5);
    Node* f = new Node(6);
    Node* g = new Node(7);
    a->left = b;
    a->right = c;
    b->left = d;
    b->right = e;
    c->left = f;
    c->right = g;



    levelOrder(a);

    return 0;
}





