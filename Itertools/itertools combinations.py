# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
sto = list(map(str, input().split(" ")))
x = 1
sto[0] = list(sto[0])
sto[0].sort()
while True:
    if x != int(sto[1])+1:
        for i in list(combinations(sto[0], x)):
            i = list(i)
            og = ""
            for h in i:
                og+=str(h)
            print(og)
        x+=1
    else:
        break