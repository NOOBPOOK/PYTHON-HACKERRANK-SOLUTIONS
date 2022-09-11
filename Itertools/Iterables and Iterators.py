# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

num = int(input())
char = list(map(str, input().split()))
x = int(input())
k = 0
ind = []
count = 0
for i in char:
    if i == "a":
        ind.append(int(k + 1))
    k += 1

f = list(combinations([x for x in range(1, num + 1)], x))
z = len(f)

for i in f:
    for y in i:
        if int(y) in ind:
            count += 1
            break

print(count / z)

