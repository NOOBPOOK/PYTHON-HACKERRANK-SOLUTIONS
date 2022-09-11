# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
ar1 = set(map(int, input().split()))
m = int(input())
ar2 = set(map(int, input().split()))

lst = []
for h in ar1.difference(ar2):
    lst.append(h)
for j in ar2.difference(ar1):
    lst.append(j)
lst.sort()
for k in lst:
    print(k)
