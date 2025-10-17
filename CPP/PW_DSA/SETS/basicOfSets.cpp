#include<iostream>
#include<unordered_set>
using namespace std;

int main(){
    unordered_set<int>s;
    s.insert(1);
    s.insert(2);
    s.insert(3);
    s.insert(4);
    s.insert(5);
    s.insert(1);
    s.insert(2);

    // for each loop
    for(int x: s){
        cout << x << "  ";
    }
    cout <<"\nsize = " << s.size() << endl;
    // s.erase(2);
    // for(int x: s){
    //     cout << x << "  ";
    // }

    if(s.find(7) != s.end()){
        cout<<"exists";
    }
    else{
        cout<<"not exists";
    }



    return 0;
}