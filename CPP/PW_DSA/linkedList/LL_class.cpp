// implementation of ll class

// insertAtEnd method : - implement a method to insert a node at the end of a linked list

#include<iostream>
using namespace std;

class Node{  // user defined data type
public:
    int val;
    Node *next;
    Node(int val){
        this->val = val;
        this->next = NULL;
    }
};

class linkedlist{ // user defined data structure
public:
    Node* head;
    Node* tail;
    int size;

    linkedlist(){
        head = tail = NULL;
        size = 0;
    }

    void insertAtEnd(int val){
        Node* temp = new Node(val);
        if(size == 0){
            head = tail = temp;
        }
        else{
            tail->next = temp;
            tail = temp;
        }
        size++;
    }

    void display(){
        Node *temp = head;
        while(temp != NULL){
            cout << temp->val << "  ";
            temp = temp->next;
        }
        cout << endl;
    }
};

int main(){
    linkedlist ll;
    ll.insertAtEnd(10);
    ll.display();
    cout <<"size :" << ll.size  << endl;

    ll.insertAtEnd(20);
    ll.display();
    cout <<"size :" << ll.size  << endl;

    ll.insertAtEnd(30);
    ll.insertAtEnd(40);
    ll.display();
    cout <<"size :" << ll.size  << endl;

    return 0;
}





// #include <iostream>
// using namespace std;

// class Node{
// public:
//     int val;
//     Node* next;

//     Node(int val){
//         this->val = val;
//         this->next = NULL;
//     }
// };

// class linkedList{
// public:
//     Node* head;
//     Node* tail;
//     int size;

//     linkedList(){
//         head = tail = NULL;
//         size = 0;
//     }

//     void insertAtEnd(int val){
//         Node* temp = new Node(val);
//         if(size == 0){
//             head = tail = temp;
//         }
//         else{
//             tail->next = temp;
//             tail = temp;
//         }
//         size++;
//     }

//     void display(){
//         Node *temp = head;
//         while(temp != NULL){
//             cout << temp->val << "  ";
//             temp = temp->next;
//         }
//         cout << endl;
//     }
// };

// int main(){

//     linkedList LL;

//     LL.insertAtEnd(10);
//     LL.display();
//     cout << " size : " << LL.size << endl << endl;

//     LL.insertAtEnd(20);
//     LL.display();
//     cout << " size : " << LL.size << endl << endl;

//     LL.insertAtEnd(30);
//     LL.display();
//     cout << " size : " << LL.size << endl << endl;

//     LL.insertAtEnd(40);
//     LL.display();
//     cout << " size : " << LL.size << endl << endl;

//     return 0;
// }