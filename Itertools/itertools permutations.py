# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

st = list(map(str, input().split(" ")))
arr = list(permutations(st[0], int(st[1])))
arr.sort()
for i in arr:
    og = ""
    for h in i:
        og+=h
    print(og)