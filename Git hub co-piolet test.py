import time

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False 
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                swapped = True 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return
        
    # Driver code to test above
    if __name__ == "__main__":
        arr = [1,8,5,10,34,12,51,14]
    target = 12
    print(bubbleSort(arr))

    length = 10000
    sorted_list = set() 
    
       
    start = time.time()  

    bubbleSort(arr)
    end = time.time()

    print("Sorted array is:")
    for i in range(len(arr)):
        print("% d" % arr[i], end=" " )

    print("\n Binary search time: ", end - start), "seconds)"
