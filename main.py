from timeit import default_timer as timer
import random

# Python program for implementation of MergeSort
#code found from https://www.geeksforgeeks.org/python-program-for-merge-sort/
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted

def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
#End of merge sort code


# Python program for implementation of InsertionSort
#code found from https://www.geeksforgeeks.org/python-program-for-insertion-sort/      

def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position        

#End of insertion sort code


# Test of Merge and Insertion sort
# original code        
def main():

    #CHANGE THIS
    # size of array
    n = 200
    #CHANGE THIS

    #how many times the loop runs
    looper = 500

    #total execution times
    mergeTotal = 0
    insertionTotal = 0

    for i in range(looper):

        #generate random list
        random_nums = [random.randint(1, 1000) for _ in range(n)]

        startM = timer()
        #sort copy of list using MergeSort
        mergeSort(random_nums.copy(), 0, n-1)
        endM = timer()
        executionMerge = endM - startM
        mergeTotal += executionMerge

        startI = timer()
        #sort copy of list using InsertionSort
        insertionSort(random_nums.copy())
        endI = timer()
        executionInsertion = endI - startI
        insertionTotal += executionInsertion

    #calculate average computation times and print
    #times by 1000 to get milliseconds
    mergeAverage = (mergeTotal / looper) * 1000
    insertionAverage = (insertionTotal / looper) * 1000
    print(f"Average Merge Sort Time taken: {mergeAverage:.6f} milliseconds")
    print(f"Average Insertion Sort Time taken: {insertionAverage:.6f} milliseconds")

    
if __name__ == "__main__":
    main()