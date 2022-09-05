# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1

# function
def binarySearch(arr, x):
    # defining the low and high borders
    low = 0
    high = len(arr)

    while low <= high:
        middle = (high + low) // 2

        # if x is greater, ignore the left half
        if arr[middle] < x:
            low = middle + 1
        
        # if x is smaller, ignore the right half
        elif arr[middle] > x:
            high = middle - 1
        else:
            return middle
    # if we reach here then the element was not found
    return -1

# array
arr = [2,4, 5, 8, 11, 13, 16]

# element searched
x = 13

# function call
result = binarySearch(arr, x)

#
if result != -1:
    print(f'element was found at: {result}')
else:
    print('element not found')