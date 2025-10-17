// #include<iostream>
// #include<vector>
// #include<limits.h>
// #define inf INT_MAX
// using namespace std;

// int helper(int n){
//     if(n == 1) return 0;
//     if(n == 2 || n == 3) return 1;

//     return 1 + min(helper(n-1), min(n%2==0 ? helper(n/2) : inf, n%3==0 ? helper(n/3) : inf));
// }

// int main(){
//     int n = 100;
//     cout << helper(n);
//     return 0;
// }


#include<iostream>
#include<vector>
#include<limits.h>
#define inf INT_MAX
using namespace std;

int main(){
    int n = 50;
    vector<int> dp(121);
    dp[1] = 0;
    dp[2] = dp[3] = 1;
    for(int i=4; i<=n; i++){
        dp[i] = 1 + min(dp[i-1], min(i%2 == 0 ? dp[i/2] : inf, i%3 == 0 ? dp[i/3] : inf));
    }
    cout << dp[n];
}