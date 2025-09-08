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

    void insertAtIdx(int idx, int val){
        if(idx <0 || idx > size) cout << "index is invalid." << endl;
        else if(idx == 0) insertAtBegining(val);
        else if(idx == size) insertAtEnd(val);
        else{
            Node* temp = head;
            Node* t = new Node(val);
            for(int i=1; i<idx; i++){
                temp = temp->next;
            }
            t->next = temp->next;
            temp->next = t;
            size++;
        }
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

    LL.insertAtBegining(30);
    LL.display();

    LL.insertAtBegining(20);
    LL.display();

    LL.insertAtBegining(10);
    LL.display();

    LL.insertAtIdx(2,25);
    LL.display();

    return 0;
}