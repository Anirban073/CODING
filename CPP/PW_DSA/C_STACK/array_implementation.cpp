#include<iostream>
using namespace std;
class stack{
public:
    int arr[5];
    int idx;
    stack(){
        idx = -1;
    }

    void push(int val){
        if(idx == 4){
            cout << "stack is full" << endl;
            return;
        }
        idx++;
        arr[idx] = val;
    }
    void pop(){
        if(idx == -1){
            cout << "stack is empty" << endl;
            return;
        }
        idx--;
    }
    int top(){
        if(idx == -1){
            cout << "stack is empty" << endl;
            return -1;
        }
        return arr[idx];
    }
    int size(){
        return idx + 1;
    }
};

int main(){
    stack st;
    cout << st.size() << endl;

    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);
    st.push(5);

    // cout << st.size() << endl;

    // cout << st.top() << endl;

    // st.pop();
    // cout << st.top() << endl;

    // while(st.size() != 0){
    //     cout << st.top() << "  ";
    //     st.pop();
    // }

    cout << st.size() << endl;
    st.push(6);
    cout << st.size() << endl;

    st.pop();
    st.pop();
    st.pop();
    st.pop();
    st.pop();
    cout << st.size() << endl;
    
    st.pop();

    cout << st.size() << endl;


    return 0;
}