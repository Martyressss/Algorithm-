def selection_sort (arr):
    n = len(arr)
    for i in range(n - 1):
        key = arr[i]
        ind = i
        for j in range (i + 1, n):
            if arr[j] > key:
                key = arr[j]
                ind = j
        if i != ind:
            arr[i], arr[ind] = arr[ind], arr[i]


arr = list(map(int, input().split()))
selection_sort(arr)
print(*arr)