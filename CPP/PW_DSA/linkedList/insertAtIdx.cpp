#include<iostream>
using namespace std;

class Node{
public:
    int val;
    Node* next;

    Node(int val){
        this->val = val;
        this->next = NULL;
    }
};

class linkedList{
public:
    Node* head;
    Node* tail;
    int size;

    linkedList(){
        head = tail = NULL;
        size = 0;
    }

    void insertAtBegining(int val){
        Node* temp = new Node(val);
        if(size == 0){
            head = tail = temp;
        }
        else{
            temp->next = head;
            head = temp;
        }
        size++;
    }

    void display(){
        Node* temp = head;
        while(temp != NULL){
            cout << temp->val << "  ";
            temp = temp->next;
        }
        cout << endl;
    }
};

int main(){
    linkedList LL;
    
    LL.insertAtBegining(40);
    LL.display();
    cout << "size : " << LL.size << endl;

    LL.insertAtBegining(30);
    LL.display();
    cout << "size : " << LL.size << endl;

    LL.insertAtBegining(20);
    LL.display();
    cout << "size : " << LL.size << endl;

    LL.insertAtBegining(10);
    LL.display();
    cout << "size : " << LL.size << endl;

    return 0;
}