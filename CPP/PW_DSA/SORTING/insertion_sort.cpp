#include<iostream>
#include <algorithm> // for std::swap

using namespace std;
int main(){
    int arr[5] = {5,1,3,2,4};
    int n = 5;

    for(int i=1; i<n; i++){
        int j = i;
        while(j > 0 && arr[j] < arr[j-1]){
            swap(arr[j-1], arr[j]);
            j--;
        }
    }

    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}