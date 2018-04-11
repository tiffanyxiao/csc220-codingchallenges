import random

def merge(arr, left, m, right):
    ''' Helper function for mergeSort(), merges two subarrays of arr'''
    # convert all parameters to ints
    left = int(left)
    m = int(m)
    right = int(right)

    n1 = m - left + 1
    n2 = right - m

    # copy data into temporary arrays L and R
    L = [arr[left+i] for i in range(0,n1)]
    R = [arr[m+1+j] for j in range(0,n2)]

    # intialize indexes of temp arrays
    i = 0
    j = 0
    k = left

    # merge temp arrays back into main array
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # copy remaining elements of L (if there are any)
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copy remaining elements of R (if there are any)
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    ''' Function implements mergeSort algorithm with helper function merge()'''
    if left < right:
        # find the middle point to divide the array into two halves
        m = (left+(right-1))/2
        # call mergesort for first half
        mergeSort(arr, left, m)
        # call mergesort for second half
        mergeSort(arr, m+1, right)
        # merge the two halves sorted
        merge(arr, left, m, right)

def compute(k):
    ''' Function creates array of random ints of size 10^k, then calls mergeSort on the array'''
    num_list = [random.randint(1,10**k) for i in range(10**k)]
    print("Given array is", num_list)
    mergeSort(num_list, 0, (10**k)-1)
    print("Sorted array is", num_list)

def main():
    ''' Function calls compute() on k = [1, ..., 7] '''
    for i in range(1,8):
        compute(i)

main()
