#include<iostream>
#include<stack>
using namespace std;

int main(){
    stack<int>st;
    st.push(10);
    st.push(20);
    st.push(30);
    st.push(40);
    // printing in reverse order and empty stack 
    // while(st.size() > 0){
    //     cout << st.top() << "  ";
    //     st.pop();
    // }


    // we will use extra stack
    stack<int>temp;
    while(st.size() > 0){
        cout << st.top() << "  ";
        temp.push(st.top());
        st.pop();
    }
    cout << endl;

    // putting element back from temp to st
    while(temp.size() > 0){
        st.push(temp.top());
        cout << st.top() << "  ";
        temp.pop();
    }
    cout << endl;
    cout << st.size() << endl;
    cout << st.top() << endl;


    return 0;
}