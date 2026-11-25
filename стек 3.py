
s = input().split()
stack = []

for x in s:
    if x in '+-*':
        b = stack.pop()
        a = stack.pop()

        if x == '+':
            stack.append(a + b)
        elif x == '-':
            stack.append(a - b)
        elif x == '*':
            stack.append(a * b)
    else:
        stack.append(int(x))

print(stack.pop())
