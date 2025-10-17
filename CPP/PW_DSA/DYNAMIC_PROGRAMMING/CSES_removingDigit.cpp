// #include<iostream>
// #include<vector>
// #include<limits.h>
// using namespace std;

// vector<int> digits(int n){
//     vector<int>v;
//     while(n > 0){
//         if(n % 10 != 0) v.push_back(n%10);
//         n /= 10;
//     }
//     return v;
// }

// int helper(int n, vector<int> &dp){
//     if(n == 0) return 0;
//     if(n <= 9) return 1;

//     if(dp[n] != -1) return dp[n];
//     vector<int>v = digits(n);

//     int result = INT_MAX;
//     for(int i=0; i<v.size(); i++){
//         if(n-v[i] >= 0){
//             result = min(result, helper(n-v[i], dp));
//         }
//     }
//     return dp[n] = 1 + result;
// }

// int main(){
//     long long n;
//     cin >> n;
//     vector<int>dp(n+5, -1);
//     cout << helper(n, dp);

//     return 0;
// }



#include<iostream>
#include<vector>
#include<limits.h>
using namespace std;

vector<int> digits(int n){
    vector<int>v;
    while(n > 0){
        if(n % 10 != 0) v.push_back(n%10);
        n /= 10;
    }
    return v;
}

int main(){
    int n;
    cin >> n;
    vector<int>dp(n+5);

    dp[0] = 0;
    for(int i=1; i<=9; i++) dp[i] = 1;

    for(int i=10; i<=n; i++){
        vector<int>v = digits(i);
        int ans = INT_MAX;
        for(int j=0; j<v.size(); j++){
            ans = min(ans, dp[i-v[j]]);
        }
        dp[i] = 1 + ans;
    }
    cout << dp[n];

    return 0;
}