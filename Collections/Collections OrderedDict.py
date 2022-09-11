# Enter your code here. Read input from STDIN. Print output to STDOUTn
from collections import OrderedDict

n = int(input())
dict = OrderedDict()
for i in range(n):
    cmd = list(input().split())
    price = cmd[len(cmd)-1]
    cmd.remove(price)
    cmd = (' '.join(cmd))
    if cmd not in dict:
        dict[str(cmd)] = int(price)
    else:
        dict[str(cmd)]+= int(price)

for x in dict:
    print(str(x) + " " + str(dict[x]))