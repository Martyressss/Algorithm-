def bubble_sort(points):
    n = len(points)
    for iter in range(n - 1):
        swapped = False
        for i in range(n - iter - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            rast1 = x1**2 + y1**2
            rast2 = x2**2 + y2**2
            if rast1 > rast2: 
                points[i], points[i + 1] = points[i + 1], points[i]
                swapped = True
        if not swapped:
            break


n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
bubble_sort(points)
for p in points:
    print(*p)