#include<iostream>
#include<vector>
using namespace std;

class stack{
public:
    vector<int>v;

    void push(int val){
        v.push_back(val);
    }
    void pop(){
        if(v.size() == 0){
            cout << "stack is empty." << endl;
            return;
        }
        v.pop_back();
    }
    int top(){
        if(v.size() == 0){
            cout << "stack is empty" << endl;
            return -1;
        }
        return v[v.size() - 1];
    }
    int size(){
        return v.size();
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

    cout << st.size() << endl;

    cout << st.top() << endl;

    st.pop();
    cout << st.top() << endl;

    while(st.size() != 0){
        cout << st.top() << "  ";
        st.pop();
    }



    return 0;
}