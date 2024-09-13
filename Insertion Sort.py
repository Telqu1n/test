import time 
import random 

def insertionSort(arr):
	n = len(arr) # Get the length of the array
	
	if n <= 1:
		return # If the array has 0 or 1 element, it is already sorted, so return

	for i in range(1, n): # Iterate over the array starting from the second element
		key = arr[i] # Store the current element as the key to be inserted in the right position
		j = i-1
		while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
			arr[j+1] = arr[j] # Shift elements to the right
			j -= 1
		arr[j+1] = key # Insert the key in the correct position

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

  # Driver code to test above    
start = time.time()  
# Generate a random list of size 1000
arr = [random.randint(1, 1000) for _ in range(1000)]

insertionSort(arr)
end = time.time()


print ("Sorted array is:")
for i in range (len(arr)):
    print("% d" % arr[i], end=" " )
    
print("\n Binary search time: ", end - start), "seconds)"



