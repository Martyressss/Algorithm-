def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    if right == -1:
        return arr[0]
    if left == len(arr):
        return arr[-1]

    if abs(x - arr[right]) <= abs(x - arr[left]):
        return arr[right]
    else:
        return arr[left]


n, k = map(int, input().split())
arr = list(map(int, input().split()))
numbers = list(map(int, input().split()))

for x in numbers:
    print(binary_search(arr, x))