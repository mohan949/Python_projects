

def binary_search(arr, find):
    left = 0
    right = len(arr)-1
    print(left, right)

    while left<=right: # left = 3 right = 4
        mid = (left+right)// 2
        if arr[mid]==find:
            return mid
        elif arr[mid]<find:
            left = mid + 1
        else:
            right = mid -1
    return -1
    
arr = [1,3,5,15,9,15,11]
find = 15
print(binary_search(arr, find))
