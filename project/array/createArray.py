from array import array

arr = array('i', [1,2,3,4])
print(arr[1])

arr.append(1)
arr.pop(1)
arr.remove(1)
print(arr)

arr = [3, 1, 4, 1, 5]
arr.sort()
print(arr)  # Output: [1, 1, 3, 4, 5]

arr.sort(reverse=True)
print(arr)  # Output: [5, 4, 3, 1, 1]
