// #include<iostream>
// #include<vector>
// #include<limits.h>
// using namespace std;

// long long helper(int n,vector<int> &dp){
//     if(n == 0) return 1;
//     if(dp[n] != -1) return dp[n];
//     long long sum = 0;
//     for(int i=1; i<=6; i++){
//         if(n - i < 0) break;
//         sum = sum + helper(n - i, dp);
//     }
//     return dp[n] = sum % 1000000007;
// }

// int main(){
//     long long n;
//     cin >> n;
//     vector<int> dp(n + 10, -1);
//     cout << helper(n, dp);
//     return 0;
// }


#include<iostream>
#include<vector>
#include<limits.h>
using namespace std;

int main(){
    long long n;
    cin >> n;
    vector<long long> dp(n+10);
    dp[0] = 1;
    for(int i=1; i<=n; i++){
        long long sum = 0;
        for(long long j=1; j<=6; j++){
            if(i-j < 0) break;
            sum = (sum + dp[i-j]) % 1000000007;
        }
        dp[i] = sum;
    }

    cout << dp[n];


    return 0;
}



