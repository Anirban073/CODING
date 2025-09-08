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

    void getAtIdx(int idx){
        if((idx >= size) || (idx < 0)){
            cout << "invalid index.";
            return;
        }
        else if(idx == 0){
            cout << "value is : " << head->val << endl;
        }
        else if(idx == size-1){
            cout << "value is : " << tail->val << endl;
        }
        else{
            Node *temp = head;
            for(int i=1; i<=idx; i++){
                temp = temp->next;
            }
            cout << "val is : " << temp->val << endl;
        }
    }

    void deleteAtHead(){
        if(size == 0) cout << "list is empty.";
        else if(size >= 1){
            head = head->next;
            size --;
        }
    }

    void deleteAtTail(){
        if(size == 0) cout << "list is empty.";
        else if(size >= 1){
            Node* temp = head;
            while(temp->next != tail){
                temp = temp->next;
            }
            temp->next = NULL;
            tail = temp;
            size--;
        }
    }

    void deleteAtIdx(int idx){
        if((idx >= size) || (idx < 0)){
            cout << "invalid index." << endl;
            return;
        }
        else if(idx == 0){
            deleteAtHead();
        }
        else if(idx == size-1){
            deleteAtTail();
        }
        else{
            Node* temp = head;
            for(int i=1; i<idx; i++){
                temp = temp->next;
            }
            temp->next = temp->next->next;
            size--;
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

    // LL.getAtIdx(4);
    LL.deleteAtIdx(2);
    LL.display();

    return 0;
}