from collections import deque
import sys
n = int(input())

def isEmpty(queue):
    if len(queue) == 0:
        return True
    else:
        return False
queue = deque([])
for i in range(n):
    cmd = list(sys.stdin.readline().strip().split(" "))
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if isEmpty(queue):
            print(1)
        else:
            print(0)
    elif not isEmpty(queue):
        if cmd[0] == "front":
            print(queue[0])
        elif cmd[0] == "back":
            print(queue[-1])
        elif cmd[0] == "pop":
                print(queue.popleft())
        elif cmd[0] == "empty":
                print(0)
    else:
        print(-1)
