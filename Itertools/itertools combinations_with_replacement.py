# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

sto = list(map(str, input().split(" ")))
sto[0] = list(sto[0])
sto[0].sort()
for i in list(combinations_with_replacement(sto[0],int(sto[1]))):
    og = ""
    for h in i:
        og+=str(h)
    print(og)