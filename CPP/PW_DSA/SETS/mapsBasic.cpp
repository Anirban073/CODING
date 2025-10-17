// method 1
// #include<iostream>
// #include<unordered_map>
// using namespace std;

// int main(){
//     pair<string, int>p1;
//     p1.first = "anirban";
//     p1.second = 21;

//     pair<string, int>p2;
//     p2.first = "kush";
//     p2.second = 20;

//     pair<string, int>p3;
//     p3.first = "jaga";
//     p3.second = 22;

//     unordered_map<string, int>m;
//     m.insert(p1);
//     m.insert(p2);
//     m.insert(p3);

//     // cout << p1.first << "  " << p1.second << endl;
//     // cout << p2.first << "  " << p2.second << endl;
//     // cout << p3.first << "  " << p3.second << endl;
//     for(pair<string, int>x: m){
//         cout << x.first<<"  "<<x.second<<endl;
//     }

//     return 0;
// }




// method 2
#include<iostream>
#include<unordered_map>
using namespace std;

int main(){
    unordered_map<string, int>m;
    m["anirban"] = 21;
    m["kush"] = 20;
    m["jaga"] = 22;

    for(pair<string, int>x: m){
        cout << x.first<<"  "<<x.second<<endl;
    }
    cout << "size = " <<m.size()<<endl;
    cout << endl;
    m.erase("jaga");

    for(pair<string, int>x: m){
        cout << x.first<<"  "<<x.second<<endl;
    }
    cout << "size = " <<m.size()<<endl;

    return 0;
}