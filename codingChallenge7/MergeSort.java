/* Java implementation of mergesort*/
public class MergeSort{
    /**
     * Helper function for mergeSort(), merges two subarrays of arr
     *
     * @param arr main array to check
     * @param left left index
     * @param mid middle index
     * @param right right index
     */
    public void merge(int arr[], int left, int mid, int right){
        int pos1 = mid - left + 1;
        int pos2 = right - mid;

        // copy data into temporary arrays L and R
        int L[] = new int [pos1];
        int R[] = new int [pos2];

        for (int i=0; i<pos1; ++i)
            L[i] = arr[left + i];
        for (int j=0; j<pos2; ++j)
            R[j] = arr[mid+1+j];

        // Initial indexes of first and second subarrays
        int i = 0;
        int j = 0;
        int k = left;

        // merge temp arrays back into main array
        while (i < pos1 && j < pos2){
            if (L[i] <= R[j]){
                arr[k] = L[i];
                i++;
            } else{
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

    /**
     * Method implements mergeSort algorithm with helper function merge
     *
     * @param arr array to sort
     * @param left left index
     * @param right right index
     */
    public void sort(int arr[], int left, int right){
        if (left < right){
            // find the middle point to divide the array into two halves
            int mid = (left+right)/2;
            // call mergesort for first half
            sort(arr, left, mid);
            // call mergesort for second half
            sort(arr , mid+1, right);
            // merge the two halves sorted
            merge(arr, left, mid, right);
        }
    }

    /** Method to print array*/
    public static void printArray(int arr[]){
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    /** Main method to drive */
    public static void main(String args[]){
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}
