def binary_search(C):
    left = 0
    right = C

    for i in range(100):
        mid = (left + right) / 2

        B = mid * mid+ mid ** 0.5
        if B < C:
            left = mid
        else:
            right = mid
    return mid


C = float(input())
x = binary_search(C)

print(f"{x:.8f}")
    
