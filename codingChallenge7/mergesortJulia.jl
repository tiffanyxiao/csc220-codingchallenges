function merge(arr, left, mid, right)
    """ Helper function for mergeSort(), merges two subarrays of arr """
    # convert all parameters to ints
    left = convert(Int64, floor(left))
    mid = convert(Int64, floor(mid))
    right = convert(Int64, floor(right))

    pos1 = mid - left + 1
    pos2 = right - mid

    # copy data into temporary arrays L and R
    L = [arr[left+i] for i in 0:pos1-1]
    R = [arr[mid+1+j] for j in 0:pos2-1]

    # intialize indexes of temp arrays
    i = 1
    j = 1
    k = left

    # merge temp arrays back into main array
    while i < pos1+1 && j < pos2+1
        if L[i] <= R[j]
            arr[k] = L[i]
            i += 1
        else
            arr[k] = R[j]
            j += 1
        end
        k += 1
    end

    # copy remaining elements of L (if there are any)
    while i < pos1+1
        arr[k] = L[i]
        i += 1
        k += 1
    end

    # copy remaining elements of R (if there are any)
    while j < pos2+1
        arr[k] = R[j]
        j += 1
        k += 1
    end
end

function mergeSort(arr, left, right)
    """ Function implements mergeSort algorithm with helper function merge() """
    if left < right
        # find the middle point to divide the array into two halves
        mid = (left+(right-1))/2
        # call mergesort for first half
        mergeSort(arr, left, mid)
        # call mergesort for second half
        mergeSort(arr, mid+1, right)
        # merge the two halves sorted
        merge(arr, left, mid, right)
    end
end

function main(arr)
    """ Function calls mergeSort on inputted array """
    println("Given array is $arr")
    mergeSort(arr, 1, length(arr))
    println("Sorted array is $arr")
end

function generateRand(k)
    """ Function to generate random ints of size 10^k """
    num_list = [rand(1: 10^k) for i in 1:(10^k)]
    return num_list
end

arr = generateRand(2)
main(arr)
