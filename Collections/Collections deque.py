# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

q = deque()
n = int(input())
for i in range(n):
    cmd = list(input().split())
    if "append" in cmd:
        q.append(int(cmd[1]))
    elif "appendleft" in cmd:
        q.appendleft(int(cmd[1]))
    elif "pop" in cmd:
        q.pop()
    elif "popleft" in cmd:
        q.popleft()

[print(x, end=" ") for x in q]
