#include<iostream>
#include<stack>
using namespace std;

int main(){
    stack<int>st;
    stack<int>gt;
    st.push(1);
    st.push(2);
    st.push(4);
    st.push(5);
    st.push(6);

    // 2nd index e 3 insert karo
    while(st.size() > 2){
        gt.push(st.top());
        st.pop();
    }
    st.push(3);
    while(gt.size() != 0){
        st.push(gt.top());
        gt.pop();
    }
    cout << endl;

    return 0;
}