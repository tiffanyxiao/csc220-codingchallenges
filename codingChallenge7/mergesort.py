import random

def merge(arr, left, mid, right):
    ''' Helper function for mergeSort(), merges two subarrays of arr'''
    # convert all parameters to ints
    left = int(left)
    mid = int(mid)
    right = int(right)

    pos1 = mid - left + 1
    pos2 = right - mid

    # copy data into temporary arrays L and R
    L = [arr[left+i] for i in range(0,pos1)]
    R = [arr[mid+1+j] for j in range(0,pos2)]

    # intialize indexes of temp arrays
    i = 0
    j = 0
    k = left

    # merge temp arrays back into main array
    while i < pos1 and j < pos2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # copy remaining elements of L (if there are any)
    while i < pos1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copy remaining elements of R (if there are any)
    while j < pos2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    ''' Function implements mergeSort algorithm with helper function merge()'''
    if left < right:
        # find the middle point to divide the array into two halves
        mid = (left+(right-1))/2
        # call mergesort for first half
        mergeSort(arr, left, mid)
        # call mergesort for second half
        mergeSort(arr, mid+1, right)
        # merge the two halves sorted
        merge(arr, left, mid, right)

def main(arr):
    """ Function calls mergeSort on inputted array """
    print("Given array is",arr)
    mergeSort(arr, 0, len(arr)-1)
    print("Sorted array is",arr)

def generateRand(k):
    """ Function to generate random ints of size 10^k """
    num_list = [random.randint(1,10**k) for i in range(10**k)]
    return num_list

arr = generateRand(2)
main(arr)
