def bubble_sort(arr):
    n = len(arr)
    k = 0
    for iter in range(n - 1):
        swapped = False
        for i in range(n - iter - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                k += 1
                swapped = True
        if not swapped:
            break
    return k

n = int(input())
arr = list(map(int, input().split()))
print(bubble_sort(arr))