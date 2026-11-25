s = input()
stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

for ch in s:
    if ch in '([{':
        stack.append(ch)
    else:
        if not stack or stack[-1] != pairs[ch]:
            print("no")
            break
        stack.pop()
else:
    if len(stack) == 0:
        print("yes")
    else:
        print("no")