def bubble_sort(arr):
    n = len(arr)
    for iter in range(n - 1):
        swapped = False
        for i in range(n - iter - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break


arr = list(map(int, input().split()))
bubble_sort(arr)
print(*arr)