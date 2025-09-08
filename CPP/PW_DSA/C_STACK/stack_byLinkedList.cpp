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

class stack{
public:
    Node* head;
    int size;

    stack(){
        head = NULL;
        size = 0;
    }

    void push(int val){
        Node* temp = new Node(val);
        temp->next = head;
        head = temp;
        size++;
    }

    void pop(){
        if(head == NULL){
            cout << "stack is empty" << endl;
            return;
        }
        head = head->next;
        size--;
    }

    int top(){
        if(head == NULL){
            cout << "stack is empty" << endl;
            return -1;
        }
        return head->val;
    }

    void print(Node* temp){
        if(temp == NULL) return;
        print(temp->next);
        cout << temp->val << "  ";
    }

    void display(){
        Node* temp = head;
        // while(temp != NULL){
        //     cout << temp->val << "  ";
        //     temp = temp->next;
        // }
        print(temp);
        cout << endl;
    }
    
};

int main(){
    stack st;
    cout << st.top() << endl;

    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);
    st.push(5);

    cout << st.top() << endl;
    st.display();
    cout << st.size << endl;

    st.push(6);
    cout << st.size << endl;
    st.display();


    return 0;
}