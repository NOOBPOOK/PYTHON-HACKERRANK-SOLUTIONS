# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

dic = defaultdict(list)
n = input().split()
for i in range(int(n[0])):
    st = input()
    dic[str(st)].append(i)

for i in range(int(n[1])):
    su = input()
    if su in dic:
        [print(x+1, end=" ") for x in dic[str(su)]]
        print(end="\n")
    else:
        print(-1)