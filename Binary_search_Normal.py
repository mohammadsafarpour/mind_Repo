# An iterative binary search function.
# It returns the location of x in the given array arr[l..r] if present, otherwise -1.
def binary_search(arr, low, high, x):
	while low <= high:
		# Find the index of the middle element
		mid = (low + high) // 2

		# Check if x is present at mid
		if arr[mid] == x:
			return mid

		# If x is greater, ignore the left half
		elif arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore the right half
		else:
			high = mid - 1

	# If we reach here, then the element was not present
	return -1

# Example usage
arr = [2, 3, 4, 10, 40]
x = 35

# Perform binary search
result = binary_search(arr, 0, len(arr) - 1, x)

# Display the result
if result != -1:
	print(f"Element {x} is present at index {result}")
else:
	print(f"Element {x} is not present in the array")
