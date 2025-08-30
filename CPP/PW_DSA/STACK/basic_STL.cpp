#include<iostream>
#include<stack>
using namespace std;

int main(){
    stack<int>st;
    cout << st.size()<<endl;
    st.push(0);
    st.push(1);
    st.push(73);
    st.push(7);
    cout << st.size() << endl;

    st.pop();
    st.size();
    cout << st.size() << endl;

    return 0;

}