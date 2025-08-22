#include<iostream>
using namespace std;

    void selectionSort(int arr[], int n){
        for(int i = 0; i < n-1; i++){
            int minIndex = i;
            for(int j = i+1; j<n; j++){
                if(arr[j] < arr[minIndex]){
                    minIndex = j;
                }
            }
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
    }

    void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

    int main() {
    int arr[15] = {64, 25, 12, 22, 11, 90, 55, 32, 67, 45, 30, 18, 10, 50, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Array original: \n";
    printArray(arr, n);
    
    selectionSort(arr, n);
    
    cout << "\nArray ordenado: \n";
    printArray(arr, n);
    


return 0;
}