#include<iostream>
using namespace std;

void helper(int a, int b){
    if(a == 0) {
        cout << "gcd : " << b << endl;
        return;
    }
    else{
        helper(b % a, a);
    }
}
int main(){
    int a = 27;
    int b = 45;
    helper(a, b);

    return 0;
}



