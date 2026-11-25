
Deque = []

while True:
    command = input().split()

    if command[0] == "push_front":
        n = int(command[1])
        Deque.insert(0, n)
        print("ok")

    elif command[0] == "push_back":
        n = int(command[1])
        Deque.append(n)
        print("ok")

    elif command[0] == "pop_front":
        if len(Deque) == 0:
            print("error")
        else:
            print(Deque.pop(0))

    elif command[0] == "pop_back":
        if len(Deque) == 0:
            print("error")
        else:
            print(Deque.pop())

    elif command[0] == "front":
        if len(Deque) == 0:
            print("error")
        else:
            print(Deque[0])

    elif command[0] == "back":
        if len(Deque) == 0:
            print("error")
        else:
            print(Deque[-1])

    elif command[0] == "size":
        print(len(Deque))

    elif command[0] == "clear":
        Deque.clear()
        print("ok")

    elif command[0] == "exit":
        print("bye")
        break
