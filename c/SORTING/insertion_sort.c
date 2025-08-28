#include<stdio.h>
int main(){
    int arr[5] = {4,1,5,2,3};
    int n = 5;

    for(int i=0; i<n-1; i++){
        int j=i+1;
        while(j > 0){
            if(arr[j] < arr[j-1]){
                int temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;

                j--;
            }
            else{
                break;
            }
        }
    }

    for(int i=0; i<n; i++){
        printf("%d \n", arr[i]);
    }
    return 0;
}