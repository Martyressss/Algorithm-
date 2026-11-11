a, b, c, d = map(int, input().split())

def f(x):
    return a * x**3 + b * x**2 + c * x + d

left = -1001
right = 1001

for i in range(200):
    mid = (left + right) / 2

    if f(mid) == 0:
        left = mid
        right = mid
        break

    if f(left) * f(mid) < 0:
        right = mid
    else:
        left = mid

print((left + right) / 2)
