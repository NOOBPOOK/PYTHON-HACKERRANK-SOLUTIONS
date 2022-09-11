# Enter your code here. Read input from STDIN. Print output to STDOUT
ma = set(map(int, input().split()))
n = int(input())
jk = False
for i in range(n):
    sa = set(map(int, input().split()))
    if len(sa) == len(ma.intersection(sa)) and len(sa)<len(ma):
        pass
    else:
        print("False")
        jk = True
        break
if not jk:
    print("True")
