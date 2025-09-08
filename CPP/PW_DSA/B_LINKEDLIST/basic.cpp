// #include<iostream>
// using namespace std;
// class Node{
// public:
//     int val;
//     Node *next;
// };
// int main(){
// // 10 20 30 40
//     Node a;
//     a.val = 10;
//     Node b;
//     b.val = 20;
//     Node c;
//     c.val = 30;
//     Node d;
//     d.val = 40;

//     // forming linked list
//     a.next = &b;
//     b.next = &c;
//     c.next = &d;
//     d.next = NULL;


//     return 0;
// }





// USING DEFAULT CONSTRUCTOR
#include<iostream>
using namespace std;

class Node{    // linked list node
public:
    int val;
    Node *next;
    Node(int val){
        this->val = val;
        this->next = NULL;
    }
};

int main(){
// 10 20 30 40
    Node a(10);

    Node b(20);

    Node c(30);

    Node d(40);

    // forming linked list
    a.next = &b;
    b.next = &c;
    c.next = &d;

    // print the values
    // cout << a.val << endl;
    // cout << a.next->val << endl;
    // cout << b.next->val << endl;
    // cout << c.next->val << endl;

    // cout << a.val << endl;
    // cout << (*(a.next)).val << endl;
    // cout << (*((*(a.next)).next)).val << endl;
    // cout << (*((*((*(a.next)).next)).next)).val << endl;

    cout << a.val << endl;
    cout << (a.next)->val << endl;
    cout << a.next->next->val << endl;
    cout << a.next->next->next->val << endl;


    return 0;
}