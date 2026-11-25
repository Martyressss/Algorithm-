
class Deque:
    def __init__(self):
        self.items = []
        self.head = 0

    def is_empty(self):
        return self.head == len(self.items)

    def push_back(self, item):
        self.items.append(item)

    def pop_front(self):
        item = self.items[self.head]
        self.head += 1

        if self.is_empty():
            self.clear()

        return item

    def pop_back(self):
        item = self.items.pop()

        if self.is_empty():
            self.clear()

        return item

    def front(self):
        return self.items[self.head]

    def back(self):
        return self.items[-1]

    def clear(self):
        self.items = []
        self.head = 0


n, k = map(int, input().split())
a = list(map(int, input().split()))

d = Deque()

for i in range(n):
    while not d.is_empty() and a[d.back()] > a[i]:
        d.pop_back()

    d.push_back(i)

    if not d.is_empty() and d.front() <= i - k:
        d.pop_front()

    if i >= k - 1:
        print(a[d.front()])
