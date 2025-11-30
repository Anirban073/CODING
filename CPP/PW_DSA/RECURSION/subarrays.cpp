#include<iostream>
#include<vector>
using namespace std;

void helper(int arr[], int n, int idx, vector<int>v){
    if(idx == n){
        for(auto ele : v){
            cout << ele << "  ";
        }
        cout << endl;
        return;
    }

    helper(arr, n, idx+1, v);
    
    if(v.size() == 0 || arr[idx-1] == v[v.size()-1]){
        v.push_back(arr[idx]);
        helper(arr, n, idx+1, v);
    }
}
int main(){
    int arr[] = {1,2,3,4};
    vector<int>v;
    int n = sizeof(arr) / sizeof(arr[0]);
    helper(arr, n, 0, v);

    return 0;
}



