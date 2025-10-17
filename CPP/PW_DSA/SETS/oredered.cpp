#include<iostream>
#include<set>
#include<map>
using namespace std;

int main(){
    // set<int>s;   // ordered set e insertion/deletion O(log N) e hoi
    // s.insert(5);
    // s.insert(1);
    // s.insert(7);
    // s.insert(0);
    // for(auto x : s){
    //     cout << x << "  ";
    // }

    // map<int, int>m;
    // m[2] = 20;
    // m[3] = 10;
    // m[1] = 30;
    map<string, int>m;
    m["b"] = 30;
    m["c"] = 10;
    m["a"] = 20;
    for(auto x : m){
        cout << x.first << "  " << x.second << endl;
    }

    return 0;
}