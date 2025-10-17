#include<iostream>
#include<vector>
#include<limits.h>
using namespace std;

int helper(vector<int>&v, int n, vector<int> &dp){
    if(n == 0) return 0;
    if(dp[n] != -2) return dp[n];
    int result = INT_MAX;
    for(auto x : v){
        if(n - x < 0) continue;
        result = min(result, helper(v, n - x, dp));
    }
    if(result == INT_MAX) return dp[n] = INT_MAX;
    return dp[n] = 1 + result;
}

int main(){
    int c , n;
    cin >> c >> n;
    vector<int>v;
    for(int i=0; i<c; i++){
        int m;
        cin >> m;
        v.push_back(m);
    }
    vector<int> dp(1000005, -2);
    int ans = helper(v, n, dp);
    if(ans != INT_MAX) cout << ans << endl;
    else cout << -1;

    return 0;
}

