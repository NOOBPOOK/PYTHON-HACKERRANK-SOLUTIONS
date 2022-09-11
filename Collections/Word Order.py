# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

dic = OrderedDict()
n = int(input())
for i in range(n):
    st = input()
    if st not in dic:
        dic[str(st)] = 1
    else:
        dic[str(st)]+=1

print(len(dic))
[print(dic[str(x)], end=" ") for x in dic]
