#include<stdlib.h>
#include<stdio.h>

void merge(int arr[], int left, int mid, int right){
    int i, j, k;
    int pos1 = mid - left + 1;
    int pos2 =  right - mid;

    // copy data into temporary arrays L and R
    int L[pos1], R[pos2];
    for (i = 0; i < pos1; i++)
        L[i] = arr[left + i];
    for (j = 0; j < pos2; j++)
        R[j] = arr[mid + 1+ j];

    // intialize indexes of temp arrays
    i = 0;
    j = 0;
    k = left;

    // merge temp arrays back into main array
    while (i < pos1 && j < pos2){
        if (L[i] <= R[j]){
            arr[k] = L[i];
            i++;
        }
        else{
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // copy remaining elements of L (if there are any)
    while (i < pos1){
        arr[k] = L[i];
        i++;
        k++;
    }

    // copy remaining elements of R (if there are any)
    while (j < pos2){
        arr[k] = R[j];
        j++;
        k++;
    }
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int left, int right){
    if (left < right){
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int mid = left+(right-left)/2;

        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid+1, right);

        merge(arr, left, mid, right);
    }
}

/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size){
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

/* Driver program to test above functions */
int main(){
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr)/sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
