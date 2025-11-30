#include<iostream>
#include<vector>
using namespace std;

void helper(int arr[], int n, int idx, vector<int>&v){
    if(idx == n){
        if(v.size() == 3){
            for(auto ele : v){
            cout << ele << "  ";
        }
        cout << endl;
        }
        return;
    }
    v.push_back(arr[idx]);
    helper(arr, n, idx+1, v);
    v.pop_back();
    helper(arr, n, idx+1, v);
}

int main(){
    int arr[] = {1,2,3,4,5};
    vector<int>v;
    int n = sizeof(arr) / sizeof(arr[0]);
    helper(arr, n, 0, v);



    return 0;
}