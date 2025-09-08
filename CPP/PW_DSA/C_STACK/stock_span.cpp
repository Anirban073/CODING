// #include<iostream>
// #include<vector>
// #include<stack>
// using namespace std;

// void stockSpan(int arr[], int n){
//     stack<int>st;
//     vector<int>ans;

//     ans.push_back(1);
//     st.push(0);

//     for(int i=1; i<n; i++){
//         while(st.size() > 0 && arr[st.top()] <= arr[i]){
//             st.pop();
//         }
//         if(st.size() != 0){
//             ans.push_back(i - st.top());
//         }
//         else{
//             ans.push_back(i+1);
//         }
//         st.push(i);
//     }

//     for(int i=0; i<n; i++){
//         cout << ans[i] << "   ";
//     }
//     cout << endl;
// }

// int main(){
//     int arr[8] = {3,1,2,7,4,6,2,3};
//     int n = sizeof(arr) / sizeof(arr[0]);

//     stockSpan(arr, n);

//     return 0;
// }


#include<iostream>
#include<vector>
#include<stack>
using namespace std;

void stockSpan(int arr[], int n){
    stack<int> st;
    vector<int> ans;

    // First element's span is always 1
    ans.push_back(1);
    st.push(0);

    for(int i=1; i<n; i++){
        // Pop smaller or equal elements
        while(!st.empty() && arr[st.top()] <= arr[i]){
            st.pop();
        }

        // If stack not empty → nearest greater element index exists
        if(!st.empty()){
            ans.push_back(i - st.top());
        }
        else{
            // No greater element → span is full length till i
            ans.push_back(i+1);
        }

        st.push(i);
    }

    // Print answer
    for(int i=0; i<n; i++){
        cout << ans[i] << "   ";
    }
    cout << endl;
}

int main(){
    int arr[8] = {3,1,2,7,4,6,2,3};
    int n = sizeof(arr) / sizeof(arr[0]);

    stockSpan(arr, n);

    return 0;
}
