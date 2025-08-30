#include<iostream>
#include<stack>
using namespace std;

void display1(stack<int>st){
    stack<int>gt;
    if(st.size() == 0) return;
    gt.push(st.top());
    cout << gt.top() << "  ";
    st.pop();
    display1(st);
    st.push(gt.top());
}

void display2(stack<int>st){
    stack<int>gt;
    if(st.size() == 0) return;
    gt.push(st.top());
    st.pop();
    display2(st);
    st.push(gt.top());
    cout << st.top() << "  ";
}

int main(){
    stack<int>st;
    stack<int>gt;
    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);
    st.push(5);
    st.push(6);

    display1(st);
    cout << endl;
    display2(st);

    return 0;
}