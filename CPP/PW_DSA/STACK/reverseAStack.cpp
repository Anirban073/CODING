#include<iostream>
#include<stack>
using namespace std;

void print(stack<int>st){  // pass by value so orginal stack e kono change hobe na
    while(st.size() != 0){
        cout << st.top() << "  ";
        st.pop();
    }
    cout << endl;
}

int main(){
    stack<int>st;
    stack<int>gt;
    stack<int>kt;

    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);

    print(st);
    while(st.size() != 0){
        gt.push(st.top());
        st.pop();
    }

    print(gt);
    while(gt.size() != 0){
        kt.push(gt.top());
        gt.pop();
    }

    print(kt);
    while(kt.size() != 0){
        st.push(kt.top());
        kt.pop();
    }
    print(st);


    return 0;
}
