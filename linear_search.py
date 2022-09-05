# linear seach algorithm

def linearSearch(arr, length, x):
    # looping the the array secuencially
    for index in range(0, length):
        if arr[index] == x:
            return index
    return -1

# array
arr = [11, 5, 8, 15, 6, 42, 2]

# searched item
x = 6

# length of the array
length = len(arr)

# setting the result of the function in the result 
result = linearSearch(arr, length, x)

if(result == -1):
    print('item not found')
else:
    print(f'item found in position: {result}')