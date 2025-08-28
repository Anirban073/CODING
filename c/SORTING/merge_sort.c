#include<stdio.h>

void merge(int arr[], int s, int m, int e){
    int temp[e-s+1];
    int idx = 0;
    int i = s;
    int j = m+1;

    while((i <= m) && j <= e){
        if(arr[i] <= arr[j]){
        temp[idx] = arr[i];
        i++;
    }
    else{
        temp[idx] = arr[j];
        j++;
    }
    idx++;
    }

    while(i <= m){
        temp[idx] = arr[i];
        idx++;
        i++;
    }
    while(j <= e){
        temp[idx] = arr[j];
        idx++;
        j++;
    }
    for(int k=0; k<idx; k++){
        arr[k+s] = temp[k];
    }
}

void mergeSort(int arr[], int s, int e){
    if(s < e){
        int m = s + ((e-s) / 2);

        mergeSort(arr, s, m);
        mergeSort(arr, m+1, e);

        merge(arr, s, m, e);
    }
}

int main(){
    int arr[6] = {12,31,35,8,32,17};
    int n = 6;
    mergeSort(arr, 0, n-1);
    for(int i=0; i<n; i++){
        printf("%d \n", arr[i]);
    }
    printf("\n");
    return 0;
}